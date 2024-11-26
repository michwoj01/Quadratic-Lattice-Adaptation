import networkx as nx
from edge import HyperEdge
from node import Node
from productions.production import Production, CannotApplyProduction

ATTR_MATCHER = "mlabel"

def _node_match(v_self, v_left):
    self_attr = v_self[ATTR_MATCHER]
    left_attr = v_left[ATTR_MATCHER]
    for k in left_attr:
        # forcing attrs only the production defines
        if k not in self_attr:
            # attr missing
            return False
        if left_attr[k] != self_attr[k]:
            # attr differs
            return False

    return True

class Graph:

    def __init__(self):
        self._G = nx.Graph()
        # list of nodes maintaining insertion order
        # (used by apply() left-side node attributes updating)
        self.ordered_nodes: list[Node] = []
        # level should be prepended to each new node in productions
        # used to generate unique labels on all recursion levels
        self.level = 1

    def add_node(self, node: Node) -> None:
        self._G.add_node(node)
        # add label to attrs for GraphMatcher
        self._G.nodes[node][ATTR_MATCHER] = node.get_matcher_label()
        # add to ordered nodes
        self.ordered_nodes.append(node)

    def add_edge(self, edge: HyperEdge):
        # we treat every edge as a hyper-edge (node in networkx)
        hyper_node = edge.get_hypernode()
        self.add_node(hyper_node)
        for node in edge.nodes:
            self._G.add_edge(hyper_node, node)

    # todo - use production metaclass mixins
    def apply(self, production: Production):
        matcher = nx.algorithms.isomorphism.GraphMatcher(
            self._G,
            production.get_left_side()._G,
            node_match=_node_match)

        # subgraph algo doesn't differentiate rotations
        # apply productions only to points not yet processed
        # key: source graph (self) set of Nodes the isomorphism will operate on
        # value: isomorphism mapping from self to left production side
        processed: dict[frozenset[Node], dict[Node, Node]] = dict()
        # set of sets is required, as nodes can border other
        # significantly different matches (can't just add them all
        # to a single set), using frozenset because set is unhashable

        for iso_map in matcher.subgraph_isomorphisms_iter():
            # NetworkX finds mapping:
            #     from G1 (main graph)
            #       to G2 (template, left side)

            self_node_set = frozenset(iso_map.keys())
            if self_node_set not in processed:
                # add nodes from current graph to processed set
                processed[self_node_set] = iso_map

        # 2-pass not to modify the graph while iterating it

        for iso_map_k, iso_map in processed.items():
            print("\nmatch")

            if not iso_map_k.issubset(self._G.nodes):
                # if the nodes disappeared from source graph,
                # then skip this mapping
                print("rejected")
                for node in iso_map_k - self._G.nodes:
                    print(f"\tmissing node {node.label}")
                continue

            self.level += 1

            # update left each match because of the
            # left.ordered_nodes modification below
            left: Graph = production.get_left_side()
            ordered_nodes_update = {}

            v_self: Node
            v_left: Node
            for v_self, v_left in iso_map.items():
                if v_left.hyper:
                    # remove only hyper-nodes
                    # normal nodes will get the same label and NetworkX
                    # will only try to update their args (not recreate them)
                    print("removing", v_self)
                    self._G.remove_node(v_self)

                i = left.ordered_nodes.index(v_left)
                ordered_nodes_update[i] = v_self#Node(v_self.x, v_self.y, v_self.label)

            # 2-pass because index() behaved wrong while updating the nodes
            for i, node in ordered_nodes_update.items():
                left.ordered_nodes[i] = node

            right: Graph = production.get_right_side(left, self.level)

            for node in right._G.nodes:
                # print("adding", node)
                if self._G.has_node(node):
                    self._substitute_node(node)
                else:
                    # call to our add_node() to update ordered_nodes list
                    self.add_node(node)

            for u, v in right._G.edges:
                # call to NetworkX add_edge() as hyper-edges
                # were created directly by the production
                self._G.add_edge(u, v)

            print("normal nodes:", len(list(filter(lambda n: not n.hyper, self._G.nodes))))
            print(" hyper nodes:", len(list(filter(lambda n:     n.hyper, self._G.nodes))))

    def _substitute_node(self, node: Node):
        """
        Node must be re-added to update properties like hanging
        """

        # match by label, save connected nodes and remove
        nb = self._G.neighbors(node)
        self._G.remove_node(node)

        # re-add node and connections
        self.add_node(node)
        for v in nb:
            self._G.add_edge(node, v)