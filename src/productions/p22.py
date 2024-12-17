from graph import Graph
from productions.production import Production
from node import Node
from edge import HyperEdge

@Production.register
class P22Example(Production):
    def get_left_side(self) -> Graph:
        g = Graph()
        n1 = Node(1, 1,       'n1', hanging=None, hanging_ignore=True) # ignore hanging when checking isomorphism
        n2 = Node(2, 1,       'n2', hanging=None, hanging_ignore=True) # ignore hanging when checking isomorphism
        n3 = Node(2, 2,       'n3', hanging=None, hanging_ignore=True) # ignore hanging when checking isomorphism
        n4 = Node(1, 2,       'n4', hanging=None, hanging_ignore=True) # ignore hanging when checking isomorphism
        n5 = Node(2, (1+2)/2, 'n5', hanging=True)
        n6 = Node(3, (1+2)/2, 'n6', hanging=None, hanging_ignore=True) # ignore hanging when checking isomorphism
        n7 = Node(3, 2,       'n7', hanging=None, hanging_ignore=True) # ignore hanging when checking isomorphism
        n8 = Node((1+2)/2, 1, 'n8', hanging=None, hanging_ignore=True) # ignore hanging when checking isomorphism
        n9 = Node(1, (1+2)/2, 'n9', hanging=None, hanging_ignore=True) # ignore hanging when checking isomorphism
        for n in [n1, n2, n3, n4, n5, n6, n7, n8, n9]:
            g.add_node(n)

        # add E edges
        g.add_edge(HyperEdge((n2, n5), 'E'))
        g.add_edge(HyperEdge((n5, n3), 'E'))
        # add Q edge
        g.add_edge(HyperEdge((n3, n5, n6, n7), 'Q', rip=True))
        # add S edge
        g.add_edge(HyperEdge((n1, n2, n3, n4, n8, n9), 'S', rip=False))

        return g


    def get_right_side(self, left: Graph, lvl: int):
        n1, n2, n3, n4, n5, n6, n7, n8, n9, hn_2_5, hn_5_3, hn_3_5_6_7, hn_1_2_3_4_8_9 = left.ordered_nodes

        g = Graph()
        for n in [n1, n2, n3, n4, n5, n6, n7, n8, n9]:
            g.add_node(n)

        # add E edges
        g.add_edge(HyperEdge((n2, n5), 'E', boundary=hn_2_5.hyperref.boundary))
        g.add_edge(HyperEdge((n5, n3), 'E', boundary=hn_5_3.hyperref.boundary))
        # add Q edge
        g.add_edge(HyperEdge((n3, n5, n6, n7), 'Q', rip=True))
        # add S edge
        g.add_edge(HyperEdge((n1, n2, n3, n4, n8, n9), 'S', rip=True))

        return g
