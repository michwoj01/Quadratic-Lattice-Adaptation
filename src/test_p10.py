from edge import HyperEdge
from graph import Graph
from node import Node
from edge import HyperEdge
from visualisation import draw
from productions.p10 import P10Example
import math


g = Graph()
n1 = Node(0.25, 0, "n1")
n2 = Node(0.75, 0, "n2")
n3 = Node(0.75, 2*math.sqrt(0.25), "n3")
n4 = Node(0.25, 2*math.sqrt(0.25), "n4")
n5 = Node(1, math.sqrt(0.25), "n5")
n6 = Node(0, math.sqrt(0.25), "n6")
n7 = Node((n1.x+n2.x)/2, (n1.y+n2.y)/2, "n7", hanging=True)

e1 = HyperEdge((n1, n7), "E")
e2 = HyperEdge((n7, n2), "E")
e3 = HyperEdge((n2, n5), "E")
e4 = HyperEdge((n4, n3), "E")
e5 = HyperEdge((n6, n4), "E")
e6 = HyperEdge((n6, n1), "E")
e7 = HyperEdge((n3, n5), "E")

e8 = HyperEdge((n3, n4, n1, n2, n5 ,n6), "S", rip=True)
g.add_node(n1)
g.add_node(n2)
g.add_node(n3)
g.add_node(n4)
g.add_node(n5)
g.add_node(n6)
g.add_node(n7)
g.add_edge(e1)
g.add_edge(e2)
g.add_edge(e3)
g.add_edge(e4)
g.add_edge(e5)
g.add_edge(e6)
g.add_edge(e7)
g.add_edge(e8)

draw(g, "test-before-production.png")
p1 = P10Example()
g.apply(p1)
draw(g, "test-after-production.png")
