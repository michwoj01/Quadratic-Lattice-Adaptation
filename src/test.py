from edge import Edge
from graph import Graph
from node import Node
from production import Production
from visualisation import draw
from p1 import P1Example

g = Graph()
n1 = Node(1, 1, True)
n2 = Node(2, 2, True)
n3 = Node(3, 3, False)
n4 = Node(4, 4, False)
e1 = Edge([n1, n2], 'n1-n2', False, False)
e2 = Edge([n3, n4], 'n3-n4', False, None)
g.add_node(n1)
g.add_node(n2)
g.add_node(n3)
g.add_node(n4)
g.add_edge(e1)
g.add_edge(e2)

# sub_g = g.get_subgraph_on_nodes([n1,n2])

# print(sub_g.nodes)

# print(g.get_edges())
# print(g.get_edges()[n1,n2])
# g.replace_edge(Edge([n1, n2], 'new-edge', False, False))
# print(g.get_edges()[n1,n2])

t1 = Node(1, 1, False)
t2 = Node(1, 1, True)

print(t1 == t2)