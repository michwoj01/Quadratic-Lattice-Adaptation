from edge import HyperEdge
from graph import Graph
from node import Node
from edge import HyperEdge
from visualisation import draw
from productions.p22 import P22Example
import math
from pathlib import Path

# ----- 1 ----- all good

g = Graph()
n1 = Node(1, 1,       'n1', hanging=None) # ignore hanging when checking isomorphism
n2 = Node(2, 1,       'n2', hanging=None) # ignore hanging when checking isomorphism
n3 = Node(2, 2,       'n3', hanging=None) # ignore hanging when checking isomorphism
n4 = Node(1, 2,       'n4', hanging=None) # ignore hanging when checking isomorphism
n5 = Node(2, (1+2)/2, 'n5', hanging=True)
n6 = Node(3, (1+2)/2, 'n6', hanging=None) # ignore hanging when checking isomorphism
n7 = Node(3, 2,       'n7', hanging=None) # ignore hanging when checking isomorphism
n8 = Node((1+2)/2, 1, 'n8', hanging=None) # ignore hanging when checking isomorphism
n9 = Node(1, (1+2)/2, 'n9', hanging=None) # ignore hanging when checking isomorphism
for n in [n1, n2, n3, n4, n5, n6, n7, n8, n9]:
    g.add_node(n)

# add E edges
g.add_edge(HyperEdge((n2, n5), 'E'))
g.add_edge(HyperEdge((n5, n3), 'E'))
# add Q edge
g.add_edge(HyperEdge((n3, n5, n6, n7), 'Q', rip=True))
# add S edge
g.add_edge(HyperEdge((n1, n2, n3, n4, n8, n9), 'S', rip=True))

# Should produce
draw(g, "test-before-production1.png")
p22 = P22Example()
g.apply(p22)
draw(g, "test-after-production1.png")

# # ----- 1.1 ----- all good with arbitrary boundaries

# g = Graph()
# n1 = Node(0, 0, "n1")
# n2 = Node(2, 0, "n2")
# n3 = Node(2, 2*math.sqrt(3), "n3")
# n4 = Node(0, 2*math.sqrt(3), "n4")
# n5 = Node(3, math.sqrt(3), "n5")
# n6 = Node(-1, math.sqrt(3), "n6")
# n7 = Node((n2.x+n5.x)/2, (n2.y+n5.y)/2, "n7", hanging=True)
# n8 = Node((n4.x+n3.x)/2, (n4.y+n3.y)/2, "n8", hanging=True)

# for n in [n1, n2, n3, n4, n5, n6, n7, n8]:
#     g.add_node(n)

# g.add_edge(HyperEdge((n1, n2), "E", boundary=True))
# g.add_edge(HyperEdge((n2, n7), "E"))
# g.add_edge(HyperEdge((n7, n5), "E"))
# g.add_edge(HyperEdge((n5, n3), "E"))
# g.add_edge(HyperEdge((n3, n8), "E", boundary=True))
# g.add_edge(HyperEdge((n8, n4), "E", boundary=True))
# g.add_edge(HyperEdge((n4, n6), "E"))
# g.add_edge(HyperEdge((n6, n1), "E"))
# g.add_edge(HyperEdge((n3, n4, n1, n2, n5, n6), "Q", rip=True))


# # Should produce
# draw(g, "test-before-production1.1.png")
# p22 = P12Example()
# g.apply(p22)
# draw(g, "test-after-production1.1.png")

# # ----- 2 ----- wrong left side shape

# g = Graph()
# n1 = Node(0, 0, "n1")
# n2 = Node(2, 0, "n2")
# n3 = Node(2, 2*math.sqrt(3), "n3")
# n4 = Node(0, 2*math.sqrt(3), "n4")
# n5 = Node(3, math.sqrt(3), "n5")
# n6 = Node(-1, math.sqrt(3), "n6")
# n7 = Node((n1.x+n2.x)/2, (n1.y+n2.y)/2, "n7", hanging=True)
# n8 = Node((n4.x+n3.x)/2, (n4.y+n3.y)/2, "n8", hanging=True)

# for n in [n1, n2, n3, n4, n5, n6, n7, n8]:
#     g.add_node(n)

# g.add_edge(HyperEdge((n1, n7), "E"))
# g.add_edge(HyperEdge((n7, n2), "E"))
# g.add_edge(HyperEdge((n2, n5), "E", boundary=True))
# g.add_edge(HyperEdge((n5, n3), "E"))
# g.add_edge(HyperEdge((n3, n8), "E"))
# g.add_edge(HyperEdge((n8, n4), "E"))
# g.add_edge(HyperEdge((n4, n6), "E"))
# g.add_edge(HyperEdge((n6, n1), "E"))
# g.add_edge(HyperEdge((n3, n4, n1, n2, n5, n6), "Q", rip=True))


# # Should not produce
# draw(g, "test-before-production2.png")
# p22 = P12Example()
# g.apply(p22)
# draw(g, "test-after-production2.png")

# # ----- 3 ----- hanging = 0 on one of the additional vertices

# g = Graph()
# n1 = Node(0, 0, "n1")
# n2 = Node(2, 0, "n2")
# n3 = Node(2, 2*math.sqrt(3), "n3")
# n4 = Node(0, 2*math.sqrt(3), "n4")
# n5 = Node(3, math.sqrt(3), "n5")
# n6 = Node(-1, math.sqrt(3), "n6")
# n7 = Node((n2.x+n5.x)/2, (n2.y+n5.y)/2, "n7", hanging=False)
# n8 = Node((n4.x+n3.x)/2, (n4.y+n3.y)/2, "n8", hanging=True)

# for n in [n1, n2, n3, n4, n5, n6, n7, n8]:
#     g.add_node(n)

# g.add_edge(HyperEdge((n1, n2), "E"))
# g.add_edge(HyperEdge((n2, n7), "E"))
# g.add_edge(HyperEdge((n7, n5), "E", boundary=True))
# g.add_edge(HyperEdge((n5, n3), "E"))
# g.add_edge(HyperEdge((n3, n8), "E"))
# g.add_edge(HyperEdge((n8, n4), "E"))
# g.add_edge(HyperEdge((n4, n6), "E"))
# g.add_edge(HyperEdge((n6, n1), "E"))
# g.add_edge(HyperEdge((n3, n4, n1, n2, n5, n6), "Q", rip=True))


# # Should not produce
# draw(g, "test-before-production3.png")
# p22 = P12Example()
# g.apply(p22)
# draw(g, "test-after-production3.png")

# # ----- 4 ----- rip = False

# g = Graph()
# n1 = Node(0, 0, "n1")
# n2 = Node(2, 0, "n2")
# n3 = Node(2, 2*math.sqrt(3), "n3")
# n4 = Node(0, 2*math.sqrt(3), "n4")
# n5 = Node(3, math.sqrt(3), "n5")
# n6 = Node(-1, math.sqrt(3), "n6")
# n7 = Node((n2.x+n5.x)/2, (n2.y+n5.y)/2, "n7", hanging=True)
# n8 = Node((n4.x+n3.x)/2, (n4.y+n3.y)/2, "n8", hanging=True)

# for n in [n1, n2, n3, n4, n5, n6, n7, n8]:
#     g.add_node(n)

# g.add_edge(HyperEdge((n1, n2), "E"))
# g.add_edge(HyperEdge((n2, n7), "E"))
# g.add_edge(HyperEdge((n7, n5), "E"))
# g.add_edge(HyperEdge((n5, n3), "E", boundary=True))
# g.add_edge(HyperEdge((n3, n8), "E"))
# g.add_edge(HyperEdge((n8, n4), "E"))
# g.add_edge(HyperEdge((n4, n6), "E"))
# g.add_edge(HyperEdge((n6, n1), "E"))
# g.add_edge(HyperEdge((n3, n4, n1, n2, n5, n6), "Q", rip=False))


# # Should not produce
# draw(g, "test-before-production4.png")
# p22 = P12Example()
# g.apply(p22)
# draw(g, "test-after-production4.png")