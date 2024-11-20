from edge import HyperEdge
from graph import Graph
from node import Node
from edge import HyperEdge
from visualisation import draw
from productions.p5 import P5

# 4(h=0)   --  E  --    3(h=0)
# |  \                 /  |
# E                       E
# |                       |
# 7(h=1)     Q(R=1)     5(h=1)
# |                       |
# E                       E
# |  /                \   |
# 1(h=0) -E- 6(h=1) -E- 2(h=0)

GP5 = Graph()
n1 = Node(0, 0, "n1", hanging=False)
n2 = Node(1, 0, "n2", hanging=False)
n3 = Node(1, 1, "n3", hanging=False)
n4 = Node(0, 1, "n4", hanging=False)
n5 = Node(1, 0.5, "n5", hanging=True)
n6 = Node(0.5, 0, "n6", hanging=True)
n7 = Node(0, 0.5, "n7", hanging=True)
for n in [n1, n2, n3, n4, n5, n6, n7]:
    GP5.add_node(n)
GP5.add_edge(HyperEdge((n1, n6), "E", boundary=True))
GP5.add_edge(HyperEdge((n6, n2), "E", boundary=True))
GP5.add_edge(HyperEdge((n2, n5), "E", boundary=True))
GP5.add_edge(HyperEdge((n5, n3), "E", boundary=True))
GP5.add_edge(HyperEdge((n3, n4), "E", boundary=True))
GP5.add_edge(HyperEdge((n4, n7), "E", boundary=True))
GP5.add_edge(HyperEdge((n7, n1), "E", boundary=True))
GP5.add_edge(HyperEdge((n3, n4, n1, n2), "Q", rip=True))

draw(GP5, "test-before-production.png")
p5 = P5()
GP5.apply(p5)
draw(GP5, "test-after-production.png")