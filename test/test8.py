from edge import HyperEdge
from graph import Graph
from node import Node
from edge import HyperEdge
from visualisation import draw
from productions.p8 import P8

# 4                   3           7
#   \              /  |  \       /
#    \            /   E    Q(R=1)
#                     |  /       \
#        Q(R=0)     5(h=1)        6
#                     |
#    /            \   E
#   /              \  |
# 1                   2

GP8 = Graph()
n1 = Node(0, 0, "n1")
n2 = Node(1, 0, "n2")
n3 = Node(1, 1, "n3")
n4 = Node(0, 1, "n4")
n5 = Node(1, 0.5, "n5", hanging=True)
n6 = Node(2, 0.5, "n6")
n7 = Node(2, 1, "n7")
for n in [n1, n2, n3, n4, n5, n6, n7]:
    GP8.add_node(n)
GP8.add_edge(HyperEdge((n2, n5), "E", boundary=False))
GP8.add_edge(HyperEdge((n5, n3), "E", boundary=False))
GP8.add_edge(HyperEdge((n3, n4, n1, n2), "Q", rip=False))
GP8.add_edge(HyperEdge((n7, n3, n5, n6), "Q", rip=True))

draw(GP8, "draw/test8-case1-stage0.png")
p8 = P8()
GP8.apply(p8)
draw(GP8, "draw/test8-case1-stage1.png")
