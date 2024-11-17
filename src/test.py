from edge import Edge
from graph import Graph
from node import Node
from production import Production
from edge import HyperEdge
from visualisation import draw
from p1 import P1Example

# X --- E --- X
# |  \     /  |
# E     Q     E
# |  /     \  |
# X --- E --- X

g = Graph()
n1 = Node(0, 0, False)
n2 = Node(1, 0, False)
n3 = Node(1, 1, False)
n4 = Node(0, 1, False)
e1 = Edge((n1, n2), "E", False, False)
e2 = Edge((n1, n4), "E", False, None)
e3 = Edge((n2, n3), "E", False, None)
e4 = Edge((n4, n2), "E", False, None)
e5 = HyperEdge((n3, n4, n1, n2), "Q", False, None)
g.add_node(n1)
g.add_node(n2)
g.add_node(n3)
g.add_node(n4)
g.add_edge(e1)
g.add_edge(e2)
g.add_edge(e3)
g.add_edge(e4)
g.add_hyperEdge(e5)

print(g.get_nodes())
print(g.get_edges())
print(g.get_hyperEdges())

t1 = Node(1, 1, False)
t2 = Node(1, 1, True)

et1 = Edge((t1, t2), "E", False, False)
et2 = Edge((t2, t1), "E", False, False)
#
print(et1 == et2)

draw(g, "test_draw.png")
