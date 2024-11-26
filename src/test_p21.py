from edge import HyperEdge
from graph import Graph
from node import Node
from edge import HyperEdge
from visualisation import draw
from productions.p21 import P21Example

g = Graph()
n1 = Node(0.2,0 , "n1")
n2 = Node(1, 0, "n2")
n3 = Node(1, 1, "n3")
n4 = Node(0.2, 1, "n4")
n5 = Node(0, 0.5, "n5")
n6 = Node(0.6, 0, "n6")
for n in [n1, n2, n3, n4, n5, n6]:
    g.add_node(n)

g.add_edge(HyperEdge((n3, n4, n1, n2, n5,n6), "Q" ,rip=False))
draw(g, "test-before-production.png")
p1 = P21Example()
g.apply(p1)
draw(g, "test-after-production.png")
