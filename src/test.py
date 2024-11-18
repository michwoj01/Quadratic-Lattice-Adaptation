from edge import Edge
from graph import Graph
from node import Node
from edge import HyperEdge
from visualisation import draw
from src.productions.p1 import P1Example

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
e4 = Edge((n4, n3), "E", False, None)
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

draw(g, "test-before-production.png")
p1 = P1Example()
if g.check_if_production_possible(p1):
    g = g.apply(p1)
draw(g, "test-after-production.png")
print(g.get_nodes())
