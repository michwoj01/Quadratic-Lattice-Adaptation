from edge import HyperEdge
from graph import Graph
from node import Node
from edge import HyperEdge
from visualisation import draw
from productions.p6 import P6Example

# 4(h=0) -E- 8(h=1) -E- 3(h=0)
# |  \                 /  |
# E                       E
# |                       |
# 7(h=1)     Q(R=1)     5(h=1)
# |                       |
# E                       E
# |  /                \   |
# 1(h=0) -E- 6(h=1) -E- 2(h=0)

GP6 = Graph()
n1 = Node(0, 0, "n1", hanging=False)
n2 = Node(1, 0, "n2", hanging=False)
n3 = Node(1, 1, "n3", hanging=False)
n4 = Node(0, 1, "n4", hanging=False)
n5 = Node(1, 0.5, "n5", hanging=True)
n6 = Node(0.5, 0, "n6", hanging=True)
n7 = Node(0, 0.5, "n7", hanging=True)
n8 = Node(0.5, 1, "n8", hanging=True)
for n in [n1, n2, n3, n4, n5, n6, n7, n8]:
    GP6.add_node(n)
GP6.add_edge(HyperEdge((n1, n6), "E", boundary=True))
GP6.add_edge(HyperEdge((n6, n2), "E", boundary=True))
GP6.add_edge(HyperEdge((n2, n5), "E", boundary=True))
GP6.add_edge(HyperEdge((n5, n3), "E", boundary=True))
GP6.add_edge(HyperEdge((n3, n8), "E", boundary=True))
GP6.add_edge(HyperEdge((n8, n4), "E", boundary=True))
GP6.add_edge(HyperEdge((n4, n7), "E", boundary=True))
GP6.add_edge(HyperEdge((n7, n1), "E", boundary=True))
GP6.add_edge(HyperEdge((n3, n4, n1, n2), "Q", rip=True))

draw(GP6, "test-before-production.png")
p6 = P6Example()
GP6.apply(p6)
draw(GP6, "test-after-production.png")
