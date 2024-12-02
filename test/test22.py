from edge import HyperEdge
from graph import Graph
from graphtest import GraphTest
from node import Node
from edge import HyperEdge
from visualisation import draw
from productions.p22 import P22Example
from pathlib import Path
import unittest

OUTPUT_DIR = Path('draw')

# Left Side
# 4                   3           7
#   \              /  |  \       /
#    \            /   E    Q(R=1)
#                     |  /       \
# 9 ---- S(R=0)     5(h=1)        6
#          |          |
#    /     |      \   E
#   /      |       \  |
# 1        8          2

# Right Side
# 4                   3           7
#   \              /  |  \       /
#    \            /   E    Q(R=1)
#                     |  /       \
# 9 ---- S(R=1)     5(h=1)        6
#          |          |
#    /     |      \   E
#   /      |       \  |
# 1        8          2



# ----- 1 ----- all good

class TestP22Case1(unittest.TestCase):
    def setUp(self):
        self.g = GraphTest()
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
            self.g.add_node(n)

        self.g.add_edge(HyperEdge((n2, n5), 'E'))
        self.g.add_edge(HyperEdge((n5, n3), 'E'))
        self.g.add_edge(HyperEdge((n3, n5, n6, n7), 'Q', rip=True))
        self.g.add_edge(HyperEdge((n1, n2, n3, n4, n8, n9), 'S', rip=False))

    def test_stage0(self):
        draw(self.g, OUTPUT_DIR / "test22-case1-stage0.png")
        ctn = self.g.count_nodes()

        self.assertEqual(ctn.normal, 9)
        self.assertEqual(ctn.normal_hanging, 1)
        self.assertEqual(ctn.hyper, 4)
        self.assertEqual(ctn.hyper_Q, 1)
        self.assertEqual(ctn.hyper_Q_rip, 1)
        self.assertEqual(ctn.hyper_S, 1)
        self.assertEqual(ctn.hyper_S_rip, 0)
        self.assertEqual(ctn.hyper_E, 2)
        self.assertEqual(ctn.hyper_E_boundary, 0)
        self.assertEqual(ctn.hyper_unknown, 0)

    def test_stage1(self):
        p22 = P22Example()
        applied = self.g.apply(p22)
        self.assertEqual(applied, 1)
    
        ctn = self.g.count_nodes()
        draw(self.g, OUTPUT_DIR / "test22-case1-stage1.png")

        self.assertEqual(ctn.normal, 9)
        self.assertEqual(ctn.normal_hanging, 1)
        self.assertEqual(ctn.hyper, 4)
        self.assertEqual(ctn.hyper_Q, 1)
        self.assertEqual(ctn.hyper_Q_rip, 1)
        self.assertEqual(ctn.hyper_S, 1)
        self.assertEqual(ctn.hyper_S_rip, 1)
        self.assertEqual(ctn.hyper_E, 2)
        self.assertEqual(ctn.hyper_E_boundary, 0)
        self.assertEqual(ctn.hyper_unknown, 0)




# ----- 2 ----- all good

class TestP22Case2(unittest.TestCase):
    def setUp(self):
        self.g = GraphTest()
        n1 = Node(1, 1,       'n1', hanging=None) # ignore hanging when checking isomorphism
        n2 = Node(2, 1,       'n2', hanging=None) # ignore hanging when checking isomorphism
        n3 = Node(2, 2,       'n3', hanging=None) # ignore hanging when checking isomorphism
        n4 = Node(1, 2,       'n4', hanging=None) # ignore hanging when checking isomorphism
        n5 = Node(2, (1+2)/2, 'n5', hanging=True)
        n6 = Node(3, (1+2)/2, 'n6', hanging=None) # ignore hanging when checking isomorphism
        n7 = Node(3, 2,       'n7', hanging=None) # ignore hanging when checking isomorphism
        n8 = Node((1+2)/2, 1, 'n8', hanging=None) # ignore hanging when checking isomorphism
        n9 = Node(1, (1+2)/2, 'n9', hanging=None) # ignore hanging when checking isomorphism
        n10 = Node(999, 999, 'n10')

        for n in [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]:
            self.g.add_node(n)

        self.g.add_edge(HyperEdge((n2, n5), 'E'))
        self.g.add_edge(HyperEdge((n5, n3), 'E'))
        self.g.add_edge(HyperEdge((n3, n5, n6, n7), 'Q', rip=True))
        self.g.add_edge(HyperEdge((n1, n2, n3, n4, n8, n9, n10), 'S', rip=False))

    def test_stage0(self):
        draw(self.g, OUTPUT_DIR / "test22-case2-stage0.png")
        ctn = self.g.count_nodes()

        self.assertEqual(ctn.normal, 10)
        self.assertEqual(ctn.normal_hanging, 1)
        self.assertEqual(ctn.hyper, 4)
        self.assertEqual(ctn.hyper_Q, 1)
        self.assertEqual(ctn.hyper_Q_rip, 1)
        self.assertEqual(ctn.hyper_S, 1)
        self.assertEqual(ctn.hyper_S_rip, 0)
        self.assertEqual(ctn.hyper_E, 2)
        self.assertEqual(ctn.hyper_E_boundary, 0)
        self.assertEqual(ctn.hyper_unknown, 0)

    def test_stage1(self):
        p22 = P22Example()
        applied = self.g.apply(p22)
        self.assertEqual(applied, 1)
    
        ctn = self.g.count_nodes()
        draw(self.g, OUTPUT_DIR / "test22-case2-stage1.png")

        self.assertEqual(ctn.normal, 10)
        self.assertEqual(ctn.normal_hanging, 1)
        self.assertEqual(ctn.hyper, 4)
        self.assertEqual(ctn.hyper_Q, 1)
        self.assertEqual(ctn.hyper_Q_rip, 1)
        self.assertEqual(ctn.hyper_S, 1)
        self.assertEqual(ctn.hyper_S_rip, 1)
        self.assertEqual(ctn.hyper_E, 2)
        self.assertEqual(ctn.hyper_E_boundary, 0)
        self.assertEqual(ctn.hyper_unknown, 0)


# ----- 3 ----- doesn't apply production

class TestP22Case3(unittest.TestCase):
    def setUp(self):
        self.g = GraphTest()
        n1 = Node(1, 1,       'n1', hanging=None) # ignore hanging when checking isomorphism
        n2 = Node(2, 1,       'n2', hanging=None) # ignore hanging when checking isomorphism
        n3 = Node(2, 2,       'n3', hanging=None) # ignore hanging when checking isomorphism
        n4 = Node(1, 2,       'n4', hanging=None) # ignore hanging when checking isomorphism
        n5 = Node(2, (1+2)/2, 'n5', hanging=True)
        n6 = Node(3, (1+2)/2, 'n6', hanging=None) # ignore hanging when checking isomorphism
        n7 = Node(3, 2,       'n7', hanging=None) # ignore hanging when checking isomorphism
        n8 = Node((1+2)/2, 1, 'n8', hanging=None) # ignore hanging when checking isomorphism

        for n in [n1, n2, n3, n4, n5, n6, n7, n8]:
            self.g.add_node(n)

        self.g.add_edge(HyperEdge((n2, n5), 'E'))
        self.g.add_edge(HyperEdge((n5, n3), 'E'))
        self.g.add_edge(HyperEdge((n3, n5, n6, n7), 'Q', rip=True))
        self.g.add_edge(HyperEdge((n1, n2, n3, n4, n8), 'S', rip=False))

    def test_stage0(self):
        draw(self.g, OUTPUT_DIR / "test22-case2-stage0.png")
        ctn = self.g.count_nodes()

        self.assertEqual(ctn.normal, 8)
        self.assertEqual(ctn.normal_hanging, 1)
        self.assertEqual(ctn.hyper, 4)
        self.assertEqual(ctn.hyper_Q, 1)
        self.assertEqual(ctn.hyper_Q_rip, 1)
        self.assertEqual(ctn.hyper_S, 1)
        self.assertEqual(ctn.hyper_S_rip, 0)
        self.assertEqual(ctn.hyper_E, 2)
        self.assertEqual(ctn.hyper_E_boundary, 0)
        self.assertEqual(ctn.hyper_unknown, 0)

    def test_stage1(self):
        p22 = P22Example()
        applied = self.g.apply(p22)
        self.assertEqual(applied, 0)
    
        ctn = self.g.count_nodes()
        draw(self.g, OUTPUT_DIR / "test22-case2-stage1.png")

        self.assertEqual(ctn.normal, 8)
        self.assertEqual(ctn.normal_hanging, 1)
        self.assertEqual(ctn.hyper, 4)
        self.assertEqual(ctn.hyper_Q, 1)
        self.assertEqual(ctn.hyper_Q_rip, 1)
        self.assertEqual(ctn.hyper_S, 1)
        self.assertEqual(ctn.hyper_S_rip, 0)
        self.assertEqual(ctn.hyper_E, 2)
        self.assertEqual(ctn.hyper_E_boundary, 0)
        self.assertEqual(ctn.hyper_unknown, 0)

