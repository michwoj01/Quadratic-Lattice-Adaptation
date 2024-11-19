from edge import HyperEdge
from graph import Graph
from node import Node
from edge import HyperEdge
from visualisation import draw
from productions.p1 import P1Example

# 4 --- E --- 7 --- E --- 3
# |  \     /  |  \     /  |
# E     Q     E     Q     E
# |  /     \  |  /     \  |
# 8 --- E --- 9 --- E --- 6
# |  \     /  |  \     /  |
# E     Q     E     Q     E
# |  /     \  |  /     \  |
# 1 --- E --- 5 --- E --- 2

g = Graph()
n1 = Node(0,   0,   "n1")
n2 = Node(1,   0,   "n2")
n3 = Node(1,   1,   "n3")
n4 = Node(0,   1,   "n4")
n5 = Node(0.5, 0,   "n5")
n6 = Node(1,   0.5, "n6")
n7 = Node(0.5, 1,   "n7")
n8 = Node(0,   0.5, "n8")
n9 = Node(0.5, 0.5, "n9")
for n in [n1, n2, n3, n4, n5, n6, n7, n8, n9]:
    g.add_node(n)

# around the border
g.add_edge(HyperEdge((n1, n5), "E", boundary=True))
g.add_edge(HyperEdge((n5, n2), "E", boundary=True))
g.add_edge(HyperEdge((n2, n6), "E", boundary=True))
g.add_edge(HyperEdge((n6, n3), "E", boundary=True))
g.add_edge(HyperEdge((n3, n7), "E", boundary=True))
g.add_edge(HyperEdge((n7, n4), "E", boundary=True))
g.add_edge(HyperEdge((n4, n8), "E", boundary=True))
g.add_edge(HyperEdge((n8, n1), "E", boundary=True))

# to center hyper-node
g.add_edge(HyperEdge((n5, n9), "E"))
g.add_edge(HyperEdge((n6, n9), "E"))
g.add_edge(HyperEdge((n7, n9), "E"))
g.add_edge(HyperEdge((n8, n9), "E"))

# Q-tag hyper-nodes
g.add_edge(HyperEdge((n1, n5, n9, n8), "Q", rip=True))
g.add_edge(HyperEdge((n5, n2, n6, n9), "Q", rip=True))
g.add_edge(HyperEdge((n8, n9, n7, n4), "Q", rip=True))
g.add_edge(HyperEdge((n9, n6, n3, n7), "Q", rip=True))

draw(g, "test-before-production.png")

p1 = P1Example()
try:
    g.apply(p1)
except Exception as e:
    print("ERROR:", e)

draw(g, "test-after-production.png")
