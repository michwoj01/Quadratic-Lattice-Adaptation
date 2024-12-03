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
        n7 = Node((n2.x + n5.x) / 2, (n2.y + n5.y) / 2, "n7", hanging=True)
        n8 = Node((n4.x + n3.x) / 2, (n4.y + n3.y) / 2, "n8", hanging=True)

        for n in [n1, n2, n3, n4, n5, n6, n7, n8]:
            self.g.add_node(n)

        self.g.add_edge(HyperEdge((n1, n2), "E"))
        self.g.add_edge(HyperEdge((n2, n7), "E"))
        self.g.add_edge(HyperEdge((n7, n5), "E"))
        self.g.add_edge(HyperEdge((n5, n3), "E"))
        self.g.add_edge(HyperEdge((n3, n8), "E"))
        self.g.add_edge(HyperEdge((n8, n4), "E"))
        self.g.add_edge(HyperEdge((n4, n6), "E"))
        self.g.add_edge(HyperEdge((n6, n1), "E"))
        self.g.add_edge(HyperEdge((n3, n4, n1, n2, n5, n6), "Q", rip=True))

    def test_stage0(self):
        draw(self.g, "draw/test12-case1-stage0.png")

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 8)
        self.assertEqual(cnt.normal_hanging, 2)
        self.assertEqual(cnt.hyper_Q, 1)
        self.assertEqual(cnt.hyper_Q_rip, 1)
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
        n7 = Node((n2.x + n5.x) / 2, (n2.y + n5.y) / 2, "n7", hanging=True)
        n8 = Node((n4.x + n3.x) / 2, (n4.y + n3.y) / 2, "n8", hanging=True)

        for n in [n1, n2, n3, n4, n5, n6, n7, n8]:
            self.g.add_node(n)

        self.g.add_edge(HyperEdge((n1, n2), "E", boundary=True))
        self.g.add_edge(HyperEdge((n2, n7), "E"))
        self.g.add_edge(HyperEdge((n7, n5), "E"))
        self.g.add_edge(HyperEdge((n5, n3), "E"))
        self.g.add_edge(HyperEdge((n3, n8), "E", boundary=True))
        self.g.add_edge(HyperEdge((n8, n4), "E", boundary=True))
        self.g.add_edge(HyperEdge((n4, n6), "E"))
        self.g.add_edge(HyperEdge((n6, n1), "E"))
        self.g.add_edge(HyperEdge((n3, n4, n1, n2, n5, n6), "Q", rip=True))

    def test_stage0(self):
        draw(self.g, "draw/test12-case2-stage0.png")

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 8)
        self.assertEqual(cnt.normal_hanging, 2)
        self.assertEqual(cnt.hyper_Q, 1)
        self.assertEqual(cnt.hyper_Q_rip, 1)
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
        n7 = Node((n1.x + n2.x) / 2, (n1.y + n2.y) / 2, "n7", hanging=True)
        n8 = Node((n4.x + n3.x) / 2, (n4.y + n3.y) / 2, "n8", hanging=True)

        for n in [n1, n2, n3, n4, n5, n6, n7, n8]:
            self.g.add_node(n)

        self.g.add_edge(HyperEdge((n1, n7), "E"))
        self.g.add_edge(HyperEdge((n7, n2), "E"))
        self.g.add_edge(HyperEdge((n2, n5), "E", boundary=True))
        self.g.add_edge(HyperEdge((n5, n3), "E"))
        self.g.add_edge(HyperEdge((n3, n8), "E"))
        self.g.add_edge(HyperEdge((n8, n4), "E"))
        self.g.add_edge(HyperEdge((n4, n6), "E"))
        self.g.add_edge(HyperEdge((n6, n1), "E"))
        self.g.add_edge(HyperEdge((n3, n4, n1, n2, n5, n6), "Q", rip=True))

    def test_stage0(self):
        draw(self.g, "draw/test12-case3-stage0.png")

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 8)
        self.assertEqual(cnt.normal_hanging, 2)
        self.assertEqual(cnt.hyper_Q, 1)
        self.assertEqual(cnt.hyper_Q_rip, 1)
        self.assertEqual(cnt.hyper_E, 8)
        self.assertEqual(cnt.hyper_E_boundary, 1)

    def test_stage1(self):
        applied = self.g.apply(self.p12)
        draw(self.g, "draw/test12-case3-stage1.png")
        self.assertEqual(applied, 0)

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 8)
        self.assertEqual(cnt.normal_hanging, 2)
        self.assertEqual(cnt.hyper_Q, 1)
        self.assertEqual(cnt.hyper_Q_rip, 1)
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
        n7 = Node((n2.x + n5.x) / 2, (n2.y + n5.y) / 2, "n7", hanging=False)
        n8 = Node((n4.x + n3.x) / 2, (n4.y + n3.y) / 2, "n8", hanging=True)

        for n in [n1, n2, n3, n4, n5, n6, n7, n8]:
            self.g.add_node(n)

        self.g.add_edge(HyperEdge((n1, n2), "E"))
        self.g.add_edge(HyperEdge((n2, n7), "E"))
        self.g.add_edge(HyperEdge((n7, n5), "E", boundary=True))
        self.g.add_edge(HyperEdge((n5, n3), "E"))
        self.g.add_edge(HyperEdge((n3, n8), "E"))
        self.g.add_edge(HyperEdge((n8, n4), "E"))
        self.g.add_edge(HyperEdge((n4, n6), "E"))
        self.g.add_edge(HyperEdge((n6, n1), "E"))
        self.g.add_edge(HyperEdge((n3, n4, n1, n2, n5, n6), "Q", rip=True))

    def test_stage0(self):
        draw(self.g, "draw/test12-case4-stage0.png")

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 8)
        self.assertEqual(cnt.normal_hanging, 1)
        self.assertEqual(cnt.hyper_Q, 1)
        self.assertEqual(cnt.hyper_Q_rip, 1)
        self.assertEqual(cnt.hyper_E, 8)
        self.assertEqual(cnt.hyper_E_boundary, 1)

    def test_stage1(self):
        applied = self.g.apply(self.p12)
        draw(self.g, "draw/test12-case4-stage1.png")
        self.assertEqual(applied, 0)

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 8)
        self.assertEqual(cnt.normal_hanging, 1)
        self.assertEqual(cnt.hyper_Q, 1)
        self.assertEqual(cnt.hyper_Q_rip, 1)
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
        n7 = Node((n2.x + n5.x) / 2, (n2.y + n5.y) / 2, "n7", hanging=True)
        n8 = Node((n4.x + n3.x) / 2, (n4.y + n3.y) / 2, "n8", hanging=True)

        for n in [n1, n2, n3, n4, n5, n6, n7, n8]:
            self.g.add_node(n)

        self.g.add_edge(HyperEdge((n1, n2), "E"))
        self.g.add_edge(HyperEdge((n2, n7), "E"))
        self.g.add_edge(HyperEdge((n7, n5), "E"))
        self.g.add_edge(HyperEdge((n5, n3), "E", boundary=True))
        self.g.add_edge(HyperEdge((n3, n8), "E"))
        self.g.add_edge(HyperEdge((n8, n4), "E"))
        self.g.add_edge(HyperEdge((n4, n6), "E"))
        self.g.add_edge(HyperEdge((n6, n1), "E"))
        self.g.add_edge(HyperEdge((n3, n4, n1, n2, n5, n6), "Q", rip=False))

    def test_stage0(self):
        draw(self.g, "draw/test12-case5-stage0.png")

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 8)
        self.assertEqual(cnt.normal_hanging, 2)
        self.assertEqual(cnt.hyper_Q, 1)
        self.assertEqual(cnt.hyper_Q_rip, 0)
        self.assertEqual(cnt.hyper_E, 8)
        self.assertEqual(cnt.hyper_E_boundary, 1)

    def test_stage1(self):
        applied = self.g.apply(self.p12)
        draw(self.g, "draw/test12-case5-stage1.png")
        self.assertEqual(applied, 0)

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 8)
        self.assertEqual(cnt.normal_hanging, 2)
        self.assertEqual(cnt.hyper_Q, 1)
        self.assertEqual(cnt.hyper_Q_rip, 0)
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
        n7 = Node((n2.x + n5.x) / 2, (n2.y + n5.y) / 2, "n7", hanging=True)
        n8 = Node((n4.x + n3.x) / 2, (n4.y + n3.y) / 2, "n8", hanging=True)
        n9 = Node((n1.x - 2), n1.y, "n9")
        n10 = Node((n6.x - 2), n6.y, "n10")
        n11 = Node((n4.x - 2), n4.y, "n11")

        for n in [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11]:
            self.g.add_node(n)

        self.g.add_edge(HyperEdge((n1, n2), "E"))
        self.g.add_edge(HyperEdge((n2, n7), "E"))
        self.g.add_edge(HyperEdge((n7, n5), "E"))
        self.g.add_edge(HyperEdge((n5, n3), "E"))
        self.g.add_edge(HyperEdge((n3, n8), "E"))
        self.g.add_edge(HyperEdge((n8, n4), "E"))
        self.g.add_edge(HyperEdge((n4, n6), "E"))
        self.g.add_edge(HyperEdge((n6, n1), "E"))
        self.g.add_edge(HyperEdge((n3, n4, n1, n2, n5, n6), "Q", rip=True))

        self.g.add_edge(HyperEdge((n1, n9), "E"))
        self.g.add_edge(HyperEdge((n6, n10), "E"))
        self.g.add_edge(HyperEdge((n4, n11), "E"))
        self.g.add_edge(HyperEdge((n9, n10), "E"))
        self.g.add_edge(HyperEdge((n10, n11), "E"))
        self.g.add_edge(HyperEdge((n4, n6, n10, n11), "Q", rip=True))


    def test_stage0(self):
        draw(self.g, "draw/test12-case6-stage0.png")

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 11)
        self.assertEqual(cnt.normal_hanging, 2)
        self.assertEqual(cnt.hyper_Q, 2)
        self.assertEqual(cnt.hyper_Q_rip, 2)
        self.assertEqual(cnt.hyper_E, 13)
        self.assertEqual(cnt.hyper_E_boundary, 0)

    def test_stage1(self):
        applied = self.g.apply(self.p12)
        draw(self.g, "draw/test12-case6-stage1.png")
        self.assertEqual(applied, 1)

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 16)
        self.assertEqual(cnt.normal_hanging, 4)
        self.assertEqual(cnt.hyper_Q, 7)
        self.assertEqual(cnt.hyper_Q_rip, 1)
        self.assertEqual(cnt.hyper_E, 23)
        self.assertEqual(cnt.hyper_E_boundary, 0)

if __name__ == '__main__':
    unittest.main()