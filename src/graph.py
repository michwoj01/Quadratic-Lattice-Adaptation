import networkx as nx
from edge import HyperEdge
from node import Node
from productions.production import Production, CannotApplyProduction

def _node_match(v, u):
    return v["label"] == u["label"]

class Graph:

    def __init__(self):
        self._G = nx.Graph()
        # list of normal nodes (not hyper-nodes),
        # maintaining insertion order (used by apply()
        # left-side node attributes updating)
        self.normal_nodes: list[Node] = []
        # level should be prepended to each new node in productions
        self.level = 1

    def add_node(self, node: Node) -> None:
        self._G.add_node(node)
        # add label to attrs for GraphMatcher
        self._G.nodes[node]["label"] = node.get_matcher_label()
        # add to normal nodes
        if not node.hyper:
            self.normal_nodes.append(node)

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
        processed: dict[frozenset[Node], dict[any]] = dict()
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

        for iso_map in processed.values():
            print("\nmatch")
            self.level += 1

            # update left each match because of the
            # left.normal_nodes modification below
            left: Graph = production.get_left_side()

            v_self: Node
            v_left: Node
            for v_self, v_left in iso_map.items():
                print("removing", v_self)
                self._G.remove_node(v_self)

                if not v_left.hyper:
                    self.normal_nodes.remove(v_self)
                    i = left.normal_nodes.index(v_left)
                    left.normal_nodes[i] = Node(v_self.x, v_self.y, v_self.label)


            right: Graph = production.get_right_side(left, self.level)

            for node in right._G.nodes:
                # print("adding", node)
                # call to out add_node() to update normal_nodes list
                self.add_node(node)

            for u, v in right._G.edges:
                # call to NetworkX add_edge() as hyper-edges
                # were created directly by the production
                self._G.add_edge(u, v)

            # break
