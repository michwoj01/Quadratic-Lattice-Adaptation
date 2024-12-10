from graphtest import GraphTest
from graph import Graph
from node import Node
from edge import HyperEdge
from visualisation import draw
from productions.p12 import P12
import math
import unittest

# ----- 1 ----- all good

class TestP12Case1(unittest.TestCase):
    def setUp(self):
        self.p12 = P12()
        self.g = GraphTest()

        n1 = Node(0, 0, "n1")
        n2 = Node(2, 0, "n2")
        n3 = Node(2, 2 * math.sqrt(3), "n3")
        n4 = Node(0, 2 * math.sqrt(3), "n4")
        n5 = Node(3, math.sqrt(3), "n5")
        n6 = Node(-1, math.sqrt(3), "n6")
        n8 = Node((n2.x + n5.x) / 2, (n2.y + n5.y) / 2, "n8", hanging=True)
        n7 = Node((n4.x + n3.x) / 2, (n4.y + n3.y) / 2, "n7", hanging=True)

        for n in [n1, n2, n3, n4, n5, n6, n7, n8]:
            self.g.add_node(n)

        self.g.add_edge(HyperEdge((n1, n2), "E"))
        self.g.add_edge(HyperEdge((n2, n8), "E"))
        self.g.add_edge(HyperEdge((n8, n5), "E"))
        self.g.add_edge(HyperEdge((n5, n3), "E"))
        self.g.add_edge(HyperEdge((n3, n7), "E"))
        self.g.add_edge(HyperEdge((n7, n4), "E"))
        self.g.add_edge(HyperEdge((n4, n6), "E"))
        self.g.add_edge(HyperEdge((n6, n1), "E"))
        self.g.add_edge(HyperEdge((n3, n4, n1, n2, n5, n6), "S", rip=True))

    def test_stage0(self):
        draw(self.g, "draw/test12-case1-stage0.png")

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 8)
        self.assertEqual(cnt.normal_hanging, 2)
        self.assertEqual(cnt.hyper_S, 1)
        self.assertEqual(cnt.hyper_S_rip, 1)
        self.assertEqual(cnt.hyper_E, 8)
        self.assertEqual(cnt.hyper_E_boundary, 0)

    def test_stage1(self):
        applied = self.g.apply(self.p12)
        draw(self.g, "draw/test12-case1-stage1.png")
        self.assertEqual(applied, 1)

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 13)
        self.assertEqual(cnt.normal_hanging, 4)
        self.assertEqual(cnt.hyper_Q, 6)
        self.assertEqual(cnt.hyper_Q_rip, 0)
        self.assertEqual(cnt.hyper_E, 18)
        self.assertEqual(cnt.hyper_E_boundary, 0)

# ----- 1.1 ----- all good with arbitrary boundaries
class TestP12Case2(unittest.TestCase):
    def setUp(self):
        self.p12 = P12()
        self.g = GraphTest()

        n1 = Node(0, 0, "n1")
        n2 = Node(2, 0, "n2")
        n3 = Node(2, 2 * math.sqrt(3), "n3")
        n4 = Node(0, 2 * math.sqrt(3), "n4")
        n5 = Node(3, math.sqrt(3), "n5")
        n6 = Node(-1, math.sqrt(3), "n6")
        n8 = Node((n2.x + n5.x) / 2, (n2.y + n5.y) / 2, "n8", hanging=True)
        n7 = Node((n4.x + n3.x) / 2, (n4.y + n3.y) / 2, "n7", hanging=True)

        for n in [n1, n2, n3, n4, n5, n6, n7, n8]:
            self.g.add_node(n)

        self.g.add_edge(HyperEdge((n1, n2), "E", boundary=True))
        self.g.add_edge(HyperEdge((n2, n8), "E"))
        self.g.add_edge(HyperEdge((n8, n5), "E"))
        self.g.add_edge(HyperEdge((n5, n3), "E"))
        self.g.add_edge(HyperEdge((n3, n7), "E", boundary=True))
        self.g.add_edge(HyperEdge((n7, n4), "E", boundary=True))
        self.g.add_edge(HyperEdge((n4, n6), "E"))
        self.g.add_edge(HyperEdge((n6, n1), "E"))
        self.g.add_edge(HyperEdge((n3, n4, n1, n2, n5, n6), "S", rip=True))

    def test_stage0(self):
        draw(self.g, "draw/test12-case2-stage0.png")

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 8)
        self.assertEqual(cnt.normal_hanging, 2)
        self.assertEqual(cnt.hyper_S, 1)
        self.assertEqual(cnt.hyper_S_rip, 1)
        self.assertEqual(cnt.hyper_E, 8)
        self.assertEqual(cnt.hyper_E_boundary, 3)

    def test_stage1(self):
        applied = self.g.apply(self.p12)
        draw(self.g, "draw/test12-case2-stage1.png")
        self.assertEqual(applied, 1)

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 13)
        self.assertEqual(cnt.normal_hanging, 3)
        self.assertEqual(cnt.hyper_Q, 6)
        self.assertEqual(cnt.hyper_Q_rip, 0)
        self.assertEqual(cnt.hyper_E, 18)
        self.assertEqual(cnt.hyper_E_boundary, 4)

# ----- 2 ----- wrong left side shape
class TestP12Case3(unittest.TestCase):
    def setUp(self):
        self.p12 = P12()
        self.g = GraphTest()

        n1 = Node(0, 0, "n1")
        n2 = Node(2, 0, "n2")
        n3 = Node(2, 2 * math.sqrt(3), "n3")
        n4 = Node(0, 2 * math.sqrt(3), "n4")
        n5 = Node(3, math.sqrt(3), "n5")
        n6 = Node(-1, math.sqrt(3), "n6")
        n8 = Node((n1.x + n2.x) / 2, (n1.y + n2.y) / 2, "n8", hanging=True)
        n7 = Node((n4.x + n3.x) / 2, (n4.y + n3.y) / 2, "n7", hanging=True)

        for n in [n1, n2, n3, n4, n5, n6, n7, n8]:
            self.g.add_node(n)

        self.g.add_edge(HyperEdge((n1, n8), "E"))
        self.g.add_edge(HyperEdge((n8, n2), "E"))
        self.g.add_edge(HyperEdge((n2, n5), "E", boundary=True))
        self.g.add_edge(HyperEdge((n5, n3), "E"))
        self.g.add_edge(HyperEdge((n3, n7), "E"))
        self.g.add_edge(HyperEdge((n7, n4), "E"))
        self.g.add_edge(HyperEdge((n4, n6), "E"))
        self.g.add_edge(HyperEdge((n6, n1), "E"))
        self.g.add_edge(HyperEdge((n3, n4, n1, n2, n5, n6), "S", rip=True))

    def test_stage0(self):
        draw(self.g, "draw/test12-case3-stage0.png")

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 8)
        self.assertEqual(cnt.normal_hanging, 2)
        self.assertEqual(cnt.hyper_S, 1)
        self.assertEqual(cnt.hyper_S_rip, 1)
        self.assertEqual(cnt.hyper_E, 8)
        self.assertEqual(cnt.hyper_E_boundary, 1)

    def test_stage1(self):
        applied = self.g.apply(self.p12)
        draw(self.g, "draw/test12-case3-stage1.png")
        self.assertEqual(applied, 0)

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 8)
        self.assertEqual(cnt.normal_hanging, 2)
        self.assertEqual(cnt.hyper_S, 1)
        self.assertEqual(cnt.hyper_S_rip, 1)
        self.assertEqual(cnt.hyper_E, 8)
        self.assertEqual(cnt.hyper_E_boundary, 1)

# ----- 3 ----- hanging = 0 on one of the additional vertices
class TestP12Case4(unittest.TestCase):
    def setUp(self):
        self.p12 = P12()
        self.g = GraphTest()

        n1 = Node(0, 0, "n1")
        n2 = Node(2, 0, "n2")
        n3 = Node(2, 2 * math.sqrt(3), "n3")
        n4 = Node(0, 2 * math.sqrt(3), "n4")
        n5 = Node(3, math.sqrt(3), "n5")
        n6 = Node(-1, math.sqrt(3), "n6")
        n8 = Node((n2.x + n5.x) / 2, (n2.y + n5.y) / 2, "n8", hanging=False)
        n7 = Node((n4.x + n3.x) / 2, (n4.y + n3.y) / 2, "n7", hanging=True)

        for n in [n1, n2, n3, n4, n5, n6, n7, n8]:
            self.g.add_node(n)

        self.g.add_edge(HyperEdge((n1, n2), "E"))
        self.g.add_edge(HyperEdge((n2, n8), "E"))
        self.g.add_edge(HyperEdge((n8, n5), "E", boundary=True))
        self.g.add_edge(HyperEdge((n5, n3), "E"))
        self.g.add_edge(HyperEdge((n3, n7), "E"))
        self.g.add_edge(HyperEdge((n7, n4), "E"))
        self.g.add_edge(HyperEdge((n4, n6), "E"))
        self.g.add_edge(HyperEdge((n6, n1), "E"))
        self.g.add_edge(HyperEdge((n3, n4, n1, n2, n5, n6), "S", rip=True))

    def test_stage0(self):
        draw(self.g, "draw/test12-case4-stage0.png")

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 8)
        self.assertEqual(cnt.normal_hanging, 1)
        self.assertEqual(cnt.hyper_S, 1)
        self.assertEqual(cnt.hyper_S_rip, 1)
        self.assertEqual(cnt.hyper_E, 8)
        self.assertEqual(cnt.hyper_E_boundary, 1)

    def test_stage1(self):
        applied = self.g.apply(self.p12)
        draw(self.g, "draw/test12-case4-stage1.png")
        self.assertEqual(applied, 0)

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 8)
        self.assertEqual(cnt.normal_hanging, 1)
        self.assertEqual(cnt.hyper_S, 1)
        self.assertEqual(cnt.hyper_S_rip, 1)
        self.assertEqual(cnt.hyper_E, 8)
        self.assertEqual(cnt.hyper_E_boundary, 1)

# ----- 4 ----- rip = False
class TestP12Case5(unittest.TestCase):
    def setUp(self):
        self.p12 = P12()
        self.g = GraphTest()

        n1 = Node(0, 0, "n1")
        n2 = Node(2, 0, "n2")
        n3 = Node(2, 2 * math.sqrt(3), "n3")
        n4 = Node(0, 2 * math.sqrt(3), "n4")
        n5 = Node(3, math.sqrt(3), "n5")
        n6 = Node(-1, math.sqrt(3), "n6")
        n8 = Node((n2.x + n5.x) / 2, (n2.y + n5.y) / 2, "n8", hanging=True)
        n7 = Node((n4.x + n3.x) / 2, (n4.y + n3.y) / 2, "n7", hanging=True)

        for n in [n1, n2, n3, n4, n5, n6, n7, n8]:
            self.g.add_node(n)

        self.g.add_edge(HyperEdge((n1, n2), "E"))
        self.g.add_edge(HyperEdge((n2, n8), "E"))
        self.g.add_edge(HyperEdge((n8, n5), "E"))
        self.g.add_edge(HyperEdge((n5, n3), "E", boundary=True))
        self.g.add_edge(HyperEdge((n3, n7), "E"))
        self.g.add_edge(HyperEdge((n7, n4), "E"))
        self.g.add_edge(HyperEdge((n4, n6), "E"))
        self.g.add_edge(HyperEdge((n6, n1), "E"))
        self.g.add_edge(HyperEdge((n3, n4, n1, n2, n5, n6), "S", rip=False))

    def test_stage0(self):
        draw(self.g, "draw/test12-case5-stage0.png")

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 8)
        self.assertEqual(cnt.normal_hanging, 2)
        self.assertEqual(cnt.hyper_S, 1)
        self.assertEqual(cnt.hyper_S_rip, 0)
        self.assertEqual(cnt.hyper_E, 8)
        self.assertEqual(cnt.hyper_E_boundary, 1)

    def test_stage1(self):
        applied = self.g.apply(self.p12)
        draw(self.g, "draw/test12-case5-stage1.png")
        self.assertEqual(applied, 0)

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 8)
        self.assertEqual(cnt.normal_hanging, 2)
        self.assertEqual(cnt.hyper_S, 1)
        self.assertEqual(cnt.hyper_S_rip, 0)
        self.assertEqual(cnt.hyper_E, 8)
        self.assertEqual(cnt.hyper_E_boundary, 1)

# ----- 5 ----- should produce - additional vertices and edges sorrounding matched shape
class TestP12Case6(unittest.TestCase):
    def setUp(self):
        self.p12 = P12()
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
        n16 = Node(n12.x, (n12.y+n13.y)/2, "n16")

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
        self.g.add_edge(HyperEdge((n3, n4, n1, n2, n5, n6), "S", rip=True))

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

        self.g.add_edge(HyperEdge((n4, n6, n10, n11), "Q", rip=True))
        self.g.add_edge(HyperEdge((n9, n6, n10, n1), "Q", rip=True))
        self.g.add_edge(HyperEdge((n9, n12, n2, n1), "Q", rip=True))
        self.g.add_edge(HyperEdge((n8, n12, n2, n16), "Q", rip=True))
        self.g.add_edge(HyperEdge((n8, n13, n5, n16), "Q", rip=True))
        self.g.add_edge(HyperEdge((n3, n13, n5, n14), "Q", rip=True))
        self.g.add_edge(HyperEdge((n3, n7, n15, n14), "Q", rip=True))
        self.g.add_edge(HyperEdge((n11, n7, n15, n4), "Q", rip=True))


    def test_stage0(self):
        draw(self.g, "draw/test12-case6-stage0.png")

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 16)
        self.assertEqual(cnt.normal_hanging, 2)
        self.assertEqual(cnt.hyper_Q, 8)
        self.assertEqual(cnt.hyper_Q_rip, 8)
        self.assertEqual(cnt.hyper_S, 1)
        self.assertEqual(cnt.hyper_S_rip, 1)
        self.assertEqual(cnt.hyper_E, 24)
        self.assertEqual(cnt.hyper_E_boundary, 8)

    def test_stage1(self):
        applied = self.g.apply(self.p12)
        draw(self.g, "draw/test12-case6-stage1.png")
        self.assertEqual(applied, 1)

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 21)
        self.assertEqual(cnt.normal_hanging, 4)
        self.assertEqual(cnt.hyper_Q, 14)
        self.assertEqual(cnt.hyper_Q_rip, 8)
        self.assertEqual(cnt.hyper_E, 34)
        self.assertEqual(cnt.hyper_E_boundary, 8)

if __name__ == '__main__':
    unittest.main()