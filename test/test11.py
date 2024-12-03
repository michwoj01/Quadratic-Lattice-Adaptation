import math
from statistics import mean

from graph import Graph
from node import Node
from edge import HyperEdge
from visualisation import draw
from productions.p11 import P11Example


# ----- 1 ----- all good

g = Graph()
n1 = Node(x=0, y=0, label="n1")
n2 = Node(x=2, y=0, label="n2")
n3 = Node(x=2, y=2 * math.sqrt(3), label="n3")
n4 = Node(x=0, y=2 * math.sqrt(3), label="n4")
n5 = Node(x=3, y=math.sqrt(3), label="n5")
n6 = Node(x=-1, y=math.sqrt(3), label="n6")
n7 = Node(x=mean((n1.x, n2.x)), y=mean((n1.y, n2.y)), label="n7", hanging=True)
n8 = Node(x=mean((n1.x, n6.x)), y=mean((n1.y, n6.y)), label="n8", hanging=True)

for n in [n1, n2, n3, n4, n5, n6, n7, n8]:
    g.add_node(n)

g.add_edge(HyperEdge((n1, n7), "E"))
g.add_edge(HyperEdge((n7, n2), "E"))
g.add_edge(HyperEdge((n2, n5), "E"))
g.add_edge(HyperEdge((n5, n3), "E"))
g.add_edge(HyperEdge((n3, n4), "E"))
g.add_edge(HyperEdge((n4, n6), "E"))
g.add_edge(HyperEdge((n6, n8), "E"))
g.add_edge(HyperEdge((n8, n1), "E"))
g.add_edge(HyperEdge((n1, n2, n5, n3, n4, n6), "Q", rip=True))


# Should produce
draw(g, "../src/test/p11-test-prod-a-_before.png")
p11 = P11Example()
g.apply(p11)
draw(g, "../src/test/p11-test-prod-a-after.png")
