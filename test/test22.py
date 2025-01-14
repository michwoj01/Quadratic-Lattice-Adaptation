from edge import HyperEdge
from graph import Graph
from graphtest import GraphTest
from node import Node
from edge import HyperEdge
from visualisation import draw
from productions.p22 import P22
from pathlib import Path
import unittest
import math

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
        p22 = P22()
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



# ----- 2 ----- all good big graph

class TestP22Case2(unittest.TestCase):
    def setUp(self):
        self.g = GraphTest()
        n1 =  Node(3,       3,       'n1',  hanging=None) # ignore hanging when checking isomorphism
        n2 =  Node(4,       3,       'n2',  hanging=None) # ignore hanging when checking isomorphism
        n3 =  Node(5,       4,       'n3',  hanging=None) # ignore hanging when checking isomorphism
        n4 =  Node(4,       5,       'n4',  hanging=None) # ignore hanging when checking isomorphism
        n5 =  Node(3,       5,       'n5',  hanging=None)
        n6 =  Node(2,       4,       'n6',  hanging=None) # ignore hanging when checking isomorphism
        n7 =  Node((2+3)/2, (3+4)/2, 'n7',  hanging=True) # ignore hanging when checking isomorphism
        n8 =  Node(1,       3,       'n8',  hanging=None) # ignore hanging when checking isomorphism
        n9 =  Node(1,       2,       'n9',  hanging=None) # ignore hanging when checking isomorphism
        n10 = Node(6,       2,       'n10', hanging=None) # ignore hanging when checking isomorphism
        n11 = Node(6,       4,       'n11', hanging=None) # ignore hanging when checking isomorphism
        n12 = Node(6,       6,       'n12', hanging=None) # ignore hanging when checking isomorphism
        n13 = Node(1,       6,       'n13', hanging=None) # ignore hanging when checking isomorphism
        n14 = Node(1,       4,       'n14', hanging=None) # ignore hanging when checking isomorphism

        for n in [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14]:
            self.g.add_node(n)

        self.g.add_edge(HyperEdge((n1, n2), 'E'))
        self.g.add_edge(HyperEdge((n2, n3), 'E'))
        self.g.add_edge(HyperEdge((n3, n4), 'E'))
        self.g.add_edge(HyperEdge((n4, n5), 'E'))
        self.g.add_edge(HyperEdge((n5, n6), 'E'))
        self.g.add_edge(HyperEdge((n6, n7), 'E'))
        self.g.add_edge(HyperEdge((n7, n1), 'E'))

        self.g.add_edge(HyperEdge((n1, n9),  'E'))
        self.g.add_edge(HyperEdge((n2, n10), 'E'))
        self.g.add_edge(HyperEdge((n3, n11), 'E'))
        self.g.add_edge(HyperEdge((n4, n12), 'E'))
        self.g.add_edge(HyperEdge((n5, n13), 'E'))
        self.g.add_edge(HyperEdge((n6, n14), 'E'))
        self.g.add_edge(HyperEdge((n7, n8),  'E'))

        self.g.add_edge(HyperEdge((n8, n9),   'E'))
        self.g.add_edge(HyperEdge((n9, n10),  'E'))
        self.g.add_edge(HyperEdge((n10, n11), 'E'))
        self.g.add_edge(HyperEdge((n11, n12), 'E'))
        self.g.add_edge(HyperEdge((n12, n13), 'E'))
        self.g.add_edge(HyperEdge((n13, n14), 'E'))
        self.g.add_edge(HyperEdge((n14, n8),  'E'))

        self.g.add_edge(HyperEdge((n1, n2, n3, n4, n5, n6), 'S', rip=False))
        self.g.add_edge(HyperEdge((n6, n7, n8, n14),        'Q', rip=True))


    def test_stage0(self):
        draw(self.g, OUTPUT_DIR / "test22-case2-stage0.png")
        ctn = self.g.count_nodes()

        self.assertEqual(ctn.normal, 14)
        self.assertEqual(ctn.normal_hanging, 1)
        self.assertEqual(ctn.hyper, 23)
        self.assertEqual(ctn.hyper_Q, 1)
        self.assertEqual(ctn.hyper_Q_rip, 1)
        self.assertEqual(ctn.hyper_S, 1)
        self.assertEqual(ctn.hyper_S_rip, 0)
        self.assertEqual(ctn.hyper_E, 21)
        self.assertEqual(ctn.hyper_E_boundary, 0)
        self.assertEqual(ctn.hyper_unknown, 0)

    def test_stage1(self):
        p22 = P22()
        applied = self.g.apply(p22)
        self.assertEqual(applied, 1)
    
        ctn = self.g.count_nodes()
        draw(self.g, OUTPUT_DIR / "test22-case2-stage1.png")

        self.assertEqual(ctn.normal, 14)
        self.assertEqual(ctn.normal_hanging, 1)
        self.assertEqual(ctn.hyper, 23)
        self.assertEqual(ctn.hyper_Q, 1)
        self.assertEqual(ctn.hyper_Q_rip, 1)
        self.assertEqual(ctn.hyper_S, 1)
        self.assertEqual(ctn.hyper_S_rip, 1)
        self.assertEqual(ctn.hyper_E, 21)
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
        draw(self.g, OUTPUT_DIR / "test22-case3-stage0.png")
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
        p22 = P22()
        applied = self.g.apply(p22)
        self.assertEqual(applied, 0)
    
        ctn = self.g.count_nodes()
        draw(self.g, OUTPUT_DIR / "test22-case3-stage1.png")

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


class TestP22Case4(unittest.TestCase):
    def setUp(self):
        self.p22 = P22()
        self.g = GraphTest()

        n1 = Node(0, 0, "n1")
        n2 = Node(2, 0, "n2")
        n3 = Node(2, 2 * math.sqrt(3), "n3")
        n4 = Node(0, 2 * math.sqrt(3), "n4")
        n5 = Node(3, math.sqrt(3), "n5")
        n6 = Node(-1, math.sqrt(3), "n6")
        n8 = Node((n2.x + n5.x) / 2, (n2.y + n5.y) / 2, "n8", hanging=True)
        n7 = Node((n4.x + n3.x) / 2, (n4.y + n3.y) / 2, "n7", hanging=True)
        n9 = Node((n1.x - 2), (n1.y - 2), "n9")
        n10 = Node(n9.x, n6.y, "n10")
        n11 = Node(n9.x, (n4.y + 2), "n11")
        n12 = Node((n2.x + 2), (n2.y - 2), "n12")
        n13 = Node(n12.x, n5.y, "n13")
        n14 = Node(n12.x, (n3.y + 2), "n14")

        n15 = Node(n7.x, n14.y, "n15")
        n16 = Node(n12.x, (n12.y + n13.y) / 2, "n16")

        for n in [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15, n16]:
            self.g.add_node(n)

        self.g.add_edge(HyperEdge((n1, n2), "E"))
        self.g.add_edge(HyperEdge((n2, n8), "E"))
        self.g.add_edge(HyperEdge((n8, n5), "E"))
        self.g.add_edge(HyperEdge((n5, n3), "E"))
        self.g.add_edge(HyperEdge((n3, n7), "E"))
        self.g.add_edge(HyperEdge((n7, n4), "E"))
        self.g.add_edge(HyperEdge((n4, n6), "E"))
        self.g.add_edge(HyperEdge((n6, n1), "E"))
        self.g.add_edge(HyperEdge((n3, n4, n1, n2, n5, n6), "S", rip=False))

        self.g.add_edge(HyperEdge((n1, n9), "E"))
        self.g.add_edge(HyperEdge((n6, n10), "E"))
        self.g.add_edge(HyperEdge((n4, n11), "E"))
        self.g.add_edge(HyperEdge((n9, n10), "E", boundary=True))
        self.g.add_edge(HyperEdge((n10, n11), "E", boundary=True))

        self.g.add_edge(HyperEdge((n2, n12), "E"))
        self.g.add_edge(HyperEdge((n5, n13), "E"))
        self.g.add_edge(HyperEdge((n3, n14), "E"))

        self.g.add_edge(HyperEdge((n12, n16), "E", boundary=True))
        self.g.add_edge(HyperEdge((n16, n13), "E", boundary=True))
        self.g.add_edge(HyperEdge((n13, n14), "E", boundary=True))

        self.g.add_edge(HyperEdge((n9, n12), "E", boundary=True))
        self.g.add_edge(HyperEdge((n14, n15), "E", boundary=True))
        self.g.add_edge(HyperEdge((n15, n11), "E", boundary=True))

        self.g.add_edge(HyperEdge((n15, n7), "E"))
        self.g.add_edge(HyperEdge((n16, n8), "E"))

        self.g.add_edge(HyperEdge((n4, n6, n10, n11), "Q", rip=False))
        self.g.add_edge(HyperEdge((n9, n6, n10, n1), "Q", rip=False))
        self.g.add_edge(HyperEdge((n9, n12, n2, n1), "Q", rip=False))
        self.g.add_edge(HyperEdge((n8, n12, n2, n16), "Q", rip=False))
        self.g.add_edge(HyperEdge((n8, n13, n5, n16), "Q", rip=False))
        self.g.add_edge(HyperEdge((n3, n13, n5, n14), "Q", rip=False))
        self.g.add_edge(HyperEdge((n3, n7, n15, n14), "Q", rip=False))
        self.g.add_edge(HyperEdge((n11, n7, n15, n4), "Q", rip=True))

    def test_stage0(self):
        draw(self.g, "draw/test22-case4-stage0.png")

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 16)
        self.assertEqual(cnt.normal_hanging, 2)
        self.assertEqual(cnt.hyper_Q, 8)
        self.assertEqual(cnt.hyper_Q_rip, 1)
        self.assertEqual(cnt.hyper_S, 1)
        self.assertEqual(cnt.hyper_S_rip, 0)
        self.assertEqual(cnt.hyper_E, 24)
        self.assertEqual(cnt.hyper_E_boundary, 8)

    def test_stage1(self):
        applied = self.g.apply(self.p22)
        draw(self.g, "draw/test22-case4-stage1.png")
        self.assertEqual(applied, 1)

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 16)
        self.assertEqual(cnt.normal_hanging, 2)
        self.assertEqual(cnt.hyper_Q, 8)
        self.assertEqual(cnt.hyper_Q_rip, 1)
        self.assertEqual(cnt.hyper_S, 1)
        self.assertEqual(cnt.hyper_S_rip, 1)
        self.assertEqual(cnt.hyper_E, 24)
        self.assertEqual(cnt.hyper_E_boundary, 8)