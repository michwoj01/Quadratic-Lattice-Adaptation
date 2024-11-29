from edge import HyperEdge
from graph import Graph
from graphtest import GraphTest
from node import Node
from edge import HyperEdge
from visualisation import draw
from productions.p22 import P22Example
from pathlib import Path

OUTPUT_DIR = Path('draw')

# ----- 1 ----- all good

g = GraphTest()
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
g.add_edge(HyperEdge((n1, n2, n3, n4, n8, n9), 'S', rip=False))

graph_nodes_count_stage0 = g.count_nodes()
# Should produce
draw(g, OUTPUT_DIR / "test22-case1-stage0.png")
p22 = P22Example()
g.apply(p22)
graph_nodes_count_stage1 = g.count_nodes()
draw(g, OUTPUT_DIR / "test22-case1-stage1.png")


assert graph_nodes_count_stage0.normal == graph_nodes_count_stage1.normal
assert graph_nodes_count_stage0.normal_hanging == graph_nodes_count_stage1.normal_hanging
assert graph_nodes_count_stage0.hyper == graph_nodes_count_stage1.hyper
assert graph_nodes_count_stage0.hyper_Q == graph_nodes_count_stage1.hyper_Q
assert graph_nodes_count_stage0.hyper_Q_rip == graph_nodes_count_stage1.hyper_Q_rip
assert graph_nodes_count_stage0.hyper_S == graph_nodes_count_stage1.hyper_S
assert graph_nodes_count_stage0.hyper_E == graph_nodes_count_stage1.hyper_E
assert graph_nodes_count_stage0.hyper_E_boundary == graph_nodes_count_stage1.hyper_E_boundary
assert graph_nodes_count_stage0.hyper_unknown == graph_nodes_count_stage1.hyper_unknown

# Graphs should differ only on count of hyper_S_rip
assert graph_nodes_count_stage0.hyper_S_rip == 0
assert graph_nodes_count_stage1.hyper_S_rip == 1



