import unittest
import math
from statistics import mean

from node import Node
from edge import HyperEdge
from visualisation import draw
from productions.p11 import P11
from graphtest import GraphTest


class TestP11Case1(unittest.TestCase):
    def setUp(self):
        self.p11 = P11()
        self.g = GraphTest()

        n1 = Node(x=0, y=0, label="n1")
        n2 = Node(x=2, y=0, label="n2")
        n3 = Node(x=2, y=2 * math.sqrt(3), label="n3")
        n4 = Node(x=0, y=2 * math.sqrt(3), label="n4")
        n5 = Node(x=3, y=math.sqrt(3), label="n5")
        n6 = Node(x=-1, y=math.sqrt(3), label="n6")
        n7 = Node(x=mean((n1.x, n2.x)), y=mean((n1.y, n2.y)), label="n7", hanging=True)
        n8 = Node(x=mean((n1.x, n6.x)), y=mean((n1.y, n6.y)), label="n8", hanging=True)

        for n in [n1, n2, n3, n4, n5, n6, n7, n8]:
            self.g.add_node(n)

        self.g.add_edge(HyperEdge((n1, n7), "E"))
        self.g.add_edge(HyperEdge((n7, n2), "E"))
        self.g.add_edge(HyperEdge((n2, n5), "E"))
        self.g.add_edge(HyperEdge((n5, n3), "E"))
        self.g.add_edge(HyperEdge((n3, n4), "E"))
        self.g.add_edge(HyperEdge((n4, n6), "E"))
        self.g.add_edge(HyperEdge((n6, n8), "E"))
        self.g.add_edge(HyperEdge((n8, n1), "E"))
        self.g.add_edge(HyperEdge((n1, n2, n5, n3, n4, n6), "S", rip=True))

    def test_stage0(self):
        draw(self.g, "draw/test11-case1-stage0.png")

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 8)
        self.assertEqual(cnt.normal_hanging, 2)
        self.assertEqual(cnt.hyper_S, 1)
        self.assertEqual(cnt.hyper_S_rip, 1)
        self.assertEqual(cnt.hyper_E, 8)
        self.assertEqual(cnt.hyper_E_boundary, 0)

    def test_stage1(self):
        applied = self.g.apply(self.p11)
        draw(self.g, "draw/test11-case1-stage1.png")
        self.assertEqual(applied, 1)

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 13)
        self.assertEqual(cnt.normal_hanging, 4)
        self.assertEqual(cnt.hyper_S, 6)
        self.assertEqual(cnt.hyper_S_rip, 0)
        self.assertEqual(cnt.hyper_E, 18)
        self.assertEqual(cnt.hyper_E_boundary, 0)


class TestP11Case2(unittest.TestCase):
    def setUp(self):
        self.p11 = P11()
        self.g = GraphTest()

        n1 = Node(x=0, y=0, label="n1")
        n2 = Node(x=2, y=0, label="n2")
        n3 = Node(x=2, y=2 * math.sqrt(3), label="n3")
        n4 = Node(x=0, y=2 * math.sqrt(3), label="n4")
        n5 = Node(x=3, y=math.sqrt(3), label="n5")
        n6 = Node(x=-1, y=math.sqrt(3), label="n6")
        n7 = Node(x=mean((n1.x, n2.x)), y=mean((n1.y, n2.y)), label="n7", hanging=True)
        n8 = Node(x=mean((n1.x, n6.x)), y=mean((n1.y, n6.y)), label="n8", hanging=True)

        for n in [n1, n2, n3, n4, n5, n6, n7, n8]:
            self.g.add_node(n)

        self.g.add_edge(HyperEdge((n1, n7), "E", boundary=True))
        self.g.add_edge(HyperEdge((n7, n2), "E", boundary=True))
        self.g.add_edge(HyperEdge((n2, n5), "E"))
        self.g.add_edge(HyperEdge((n5, n3), "E"))
        self.g.add_edge(HyperEdge((n3, n4), "E", boundary=True))
        self.g.add_edge(HyperEdge((n4, n6), "E"))
        self.g.add_edge(HyperEdge((n6, n8), "E"))
        self.g.add_edge(HyperEdge((n8, n1), "E"))
        self.g.add_edge(HyperEdge((n1, n2, n5, n3, n4, n6), "S", rip=True))

    def test_stage0(self):
        draw(self.g, "draw/test11-case2-stage0.png")

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 8)
        self.assertEqual(cnt.normal_hanging, 2)
        self.assertEqual(cnt.hyper_S, 1)
        self.assertEqual(cnt.hyper_S_rip, 1)
        self.assertEqual(cnt.hyper_E, 8)
        self.assertEqual(cnt.hyper_E_boundary, 3)

    def test_stage1(self):
        applied = self.g.apply(self.p11)
        draw(self.g, "draw/test11-case2-stage1.png")
        self.assertEqual(applied, 1)

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 13)
        self.assertEqual(cnt.normal_hanging, 3)
        self.assertEqual(cnt.hyper_S, 6)
        self.assertEqual(cnt.hyper_S_rip, 0)
        self.assertEqual(cnt.hyper_E, 18)
        self.assertEqual(cnt.hyper_E_boundary, 4)


class TestP11Case3(unittest.TestCase):
    def setUp(self):
        self.p11 = P11()
        self.g = GraphTest()

        n1 = Node(x=0, y=0, label="n1")
        n2 = Node(x=2, y=0, label="n2")
        n3 = Node(x=2, y=2 * math.sqrt(3), label="n3")
        n4 = Node(x=0, y=2 * math.sqrt(3), label="n4")
        n5 = Node(x=3, y=math.sqrt(3), label="n5")
        n6 = Node(x=-1, y=math.sqrt(3), label="n6")
        n7 = Node(x=mean((n1.x, n2.x)), y=mean((n1.y, n2.y)), label="n7", hanging=True)
        n8 = Node(x=mean((n4.x, n6.x)), y=mean((n4.y, n6.y)), label="n8", hanging=True)

        for n in [n1, n2, n3, n4, n5, n6, n7, n8]:
            self.g.add_node(n)

        self.g.add_edge(HyperEdge((n1, n7), "E"))
        self.g.add_edge(HyperEdge((n7, n2), "E"))
        self.g.add_edge(HyperEdge((n2, n5), "E", boundary=True))
        self.g.add_edge(HyperEdge((n5, n3), "E"))
        self.g.add_edge(HyperEdge((n3, n4), "E"))
        self.g.add_edge(HyperEdge((n4, n8), "E"))
        self.g.add_edge(HyperEdge((n8, n6), "E"))
        self.g.add_edge(HyperEdge((n6, n1), "E"))
        self.g.add_edge(HyperEdge((n1, n2, n5, n3, n4, n6), "S", rip=True))

    def test_stage0(self):
        draw(self.g, "draw/test11-case3-stage0.png")

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 8)
        self.assertEqual(cnt.normal_hanging, 2)
        self.assertEqual(cnt.hyper_S, 1)
        self.assertEqual(cnt.hyper_S_rip, 1)
        self.assertEqual(cnt.hyper_E, 8)
        self.assertEqual(cnt.hyper_E_boundary, 1)

    def test_stage1(self):
        applied = self.g.apply(self.p11)
        draw(self.g, "draw/test11-case3-stage1.png")
        self.assertEqual(applied, 0)

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 8)
        self.assertEqual(cnt.normal_hanging, 2)
        self.assertEqual(cnt.hyper_S, 1)
        self.assertEqual(cnt.hyper_S_rip, 1)
        self.assertEqual(cnt.hyper_E, 8)
        self.assertEqual(cnt.hyper_E_boundary, 1)


class TestP11Case4(unittest.TestCase):
    def setUp(self):
        self.p11 = P11()
        self.g = GraphTest()

        n1 = Node(x=0, y=0, label="n1")
        n2 = Node(x=2, y=0, label="n2")
        n3 = Node(x=2, y=2 * math.sqrt(3), label="n3")
        n4 = Node(x=0, y=2 * math.sqrt(3), label="n4")
        n5 = Node(x=3, y=math.sqrt(3), label="n5")
        n6 = Node(x=-1, y=math.sqrt(3), label="n6")
        n7 = Node(x=mean((n1.x, n2.x)), y=mean((n1.y, n2.y)), label="n7", hanging=True)
        n8 = Node(x=mean((n1.x, n6.x)), y=mean((n1.y, n6.y)), label="n8", hanging=False)

        for n in [n1, n2, n3, n4, n5, n6, n7, n8]:
            self.g.add_node(n)

        self.g.add_edge(HyperEdge((n1, n7), "E"))
        self.g.add_edge(HyperEdge((n7, n2), "E", boundary=True))
        self.g.add_edge(HyperEdge((n2, n5), "E"))
        self.g.add_edge(HyperEdge((n5, n3), "E"))
        self.g.add_edge(HyperEdge((n3, n4), "E"))
        self.g.add_edge(HyperEdge((n4, n6), "E"))
        self.g.add_edge(HyperEdge((n6, n8), "E"))
        self.g.add_edge(HyperEdge((n8, n1), "E"))
        self.g.add_edge(HyperEdge((n1, n2, n5, n3, n4, n6), "S", rip=True))

    def test_stage0(self):
        draw(self.g, "draw/test11-case4-stage0.png")

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 8)
        self.assertEqual(cnt.normal_hanging, 1)
        self.assertEqual(cnt.hyper_S, 1)
        self.assertEqual(cnt.hyper_S_rip, 1)
        self.assertEqual(cnt.hyper_E, 8)
        self.assertEqual(cnt.hyper_E_boundary, 1)

    def test_stage1(self):
        applied = self.g.apply(self.p11)
        draw(self.g, "draw/test11-case4-stage1.png")
        self.assertEqual(applied, 0)

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 8)
        self.assertEqual(cnt.normal_hanging, 1)
        self.assertEqual(cnt.hyper_S, 1)
        self.assertEqual(cnt.hyper_S_rip, 1)
        self.assertEqual(cnt.hyper_E, 8)
        self.assertEqual(cnt.hyper_E_boundary, 1)


class TestP11Case5(unittest.TestCase):
    def setUp(self):
        self.p11 = P11()
        self.g = GraphTest()

        n1 = Node(x=0, y=0, label="n1")
        n2 = Node(x=2, y=0, label="n2")
        n3 = Node(x=2, y=2 * math.sqrt(3), label="n3")
        n4 = Node(x=0, y=2 * math.sqrt(3), label="n4")
        n5 = Node(x=3, y=math.sqrt(3), label="n5")
        n6 = Node(x=-1, y=math.sqrt(3), label="n6")
        n7 = Node(x=mean((n1.x, n2.x)), y=mean((n1.y, n2.y)), label="n7", hanging=True)
        n8 = Node(x=mean((n1.x, n6.x)), y=mean((n1.y, n6.y)), label="n8", hanging=True)

        for n in [n1, n2, n3, n4, n5, n6, n7, n8]:
            self.g.add_node(n)

        self.g.add_edge(HyperEdge((n1, n7), "E"))
        self.g.add_edge(HyperEdge((n7, n2), "E"))
        self.g.add_edge(HyperEdge((n2, n5), "E"))
        self.g.add_edge(HyperEdge((n5, n3), "E", boundary=True))
        self.g.add_edge(HyperEdge((n3, n4), "E"))
        self.g.add_edge(HyperEdge((n4, n6), "E"))
        self.g.add_edge(HyperEdge((n6, n8), "E"))
        self.g.add_edge(HyperEdge((n8, n1), "E"))
        self.g.add_edge(HyperEdge((n1, n2, n5, n3, n4, n6), "S", rip=False))

    def test_stage0(self):
        draw(self.g, "draw/test11-case5-stage0.png")

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 8)
        self.assertEqual(cnt.normal_hanging, 2)
        self.assertEqual(cnt.hyper_S, 1)
        self.assertEqual(cnt.hyper_S_rip, 0)
        self.assertEqual(cnt.hyper_E, 8)
        self.assertEqual(cnt.hyper_E_boundary, 1)

    def test_stage1(self):
        applied = self.g.apply(self.p11)
        draw(self.g, "draw/test11-case5-stage1.png")
        self.assertEqual(applied, 0)

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 8)
        self.assertEqual(cnt.normal_hanging, 2)
        self.assertEqual(cnt.hyper_S, 1)
        self.assertEqual(cnt.hyper_S_rip, 0)
        self.assertEqual(cnt.hyper_E, 8)
        self.assertEqual(cnt.hyper_E_boundary, 1)


class TestP11Case6(unittest.TestCase):
    def setUp(self):
        self.p11 = P11()
        self.g = GraphTest()

        n1 = Node(x=0, y=0, label="n1")
        n2 = Node(x=2, y=0, label="n2")
        n3 = Node(x=2, y=2 * math.sqrt(3), label="n3")
        n4 = Node(x=0, y=2 * math.sqrt(3), label="n4")
        n5 = Node(x=3, y=math.sqrt(3), label="n5")
        n6 = Node(x=-1, y=math.sqrt(3), label="n6")
        n7 = Node(x=mean((n1.x, n2.x)), y=mean((n1.y, n2.y)), label="n7", hanging=True)
        n8 = Node(x=mean((n1.x, n6.x)), y=mean((n1.y, n6.y)), label="n8", hanging=True)
        n9 = Node(x=(n1.x - 2), y=n1.y, label="n9")
        n10 = Node(x=(n6.x - 2), y=n6.y, label="n10")
        n11 = Node(x=(n4.x - 2), y=n4.y, label="n11")

        for n in [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11]:
            self.g.add_node(n)

        self.g.add_edge(HyperEdge((n1, n7), "E"))
        self.g.add_edge(HyperEdge((n7, n2), "E"))
        self.g.add_edge(HyperEdge((n2, n5), "E"))
        self.g.add_edge(HyperEdge((n5, n3), "E"))
        self.g.add_edge(HyperEdge((n3, n4), "E"))
        self.g.add_edge(HyperEdge((n4, n6), "E"))
        self.g.add_edge(HyperEdge((n6, n8), "E"))
        self.g.add_edge(HyperEdge((n8, n1), "E"))
        self.g.add_edge(HyperEdge((n1, n2, n5, n3, n4, n6), "S", rip=True))

        self.g.add_edge(HyperEdge((n1, n9), "E"))
        self.g.add_edge(HyperEdge((n6, n10), "E"))
        self.g.add_edge(HyperEdge((n4, n11), "E"))
        self.g.add_edge(HyperEdge((n9, n10), "E"))
        self.g.add_edge(HyperEdge((n10, n11), "E"))
        self.g.add_edge(HyperEdge((n4, n6, n10, n11), "Q", rip=True))

    def test_stage0(self):
        draw(self.g, "draw/test11-case6-stage0.png")

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 11)
        self.assertEqual(cnt.normal_hanging, 2)
        self.assertEqual(cnt.hyper_S, 1)
        self.assertEqual(cnt.hyper_S_rip, 1)
        self.assertEqual(cnt.hyper_Q, 1)
        self.assertEqual(cnt.hyper_Q_rip, 1)
        self.assertEqual(cnt.hyper_E, 13)
        self.assertEqual(cnt.hyper_E_boundary, 0)

    def test_stage1(self):
        applied = self.g.apply(self.p11)
        draw(self.g, "draw/test11-case6-stage1.png")
        self.assertEqual(applied, 1)

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 16)
        self.assertEqual(cnt.normal_hanging, 4)
        self.assertEqual(cnt.hyper_S, 6)
        self.assertEqual(cnt.hyper_S_rip, 0)
        self.assertEqual(cnt.hyper_Q, 1)
        self.assertEqual(cnt.hyper_Q_rip, 1)
        self.assertEqual(cnt.hyper_E, 23)
        self.assertEqual(cnt.hyper_E_boundary, 0)


class TestP11Case7(unittest.TestCase):
    def setUp(self):
        self.p11 = P11()
        self.g = GraphTest()

        n1 = Node(x=0, y=0, label="n1")
        n2 = Node(x=2, y=0, label="n2")
        n3 = Node(x=2, y=2 * math.sqrt(3), label="n3")
        n4 = Node(x=0, y=2 * math.sqrt(3), label="n4")
        n5 = Node(x=3, y=math.sqrt(3), label="n5")
        n6 = Node(x=-1, y=math.sqrt(3), label="n6")
        n7 = Node(x=mean((n1.x, n2.x)), y=mean((n1.y, n2.y)), label="n7", hanging=True)
        n8 = Node(x=mean((n1.x, n6.x)), y=mean((n1.y, n6.y)), label="n8", hanging=True)

        n9 = Node(x=1.5, y=-math.sqrt(3) / 2, label="n9")
        n10 = Node(x=0.5, y=-math.sqrt(3) / 2, label="n10")
        n11 = Node(x=-0.5, y=-math.sqrt(3) / 2, label="n11")

        n12 = Node(x=(n1.x - 2), y=n1.y, label="n12")
        n13 = Node(x=(n6.x - 2), y=n6.y, label="n13")
        n14 = Node(x=(n4.x - 2), y=n4.y, label="n14")


        for n in [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14]:
            self.g.add_node(n)

        self.g.add_edge(HyperEdge((n1, n7), "E"))
        self.g.add_edge(HyperEdge((n7, n2), "E"))
        self.g.add_edge(HyperEdge((n2, n5), "E", boundary=True))
        self.g.add_edge(HyperEdge((n5, n3), "E", boundary=True))
        self.g.add_edge(HyperEdge((n3, n4), "E", boundary=True))
        self.g.add_edge(HyperEdge((n4, n6), "E"))
        self.g.add_edge(HyperEdge((n6, n8), "E"))
        self.g.add_edge(HyperEdge((n8, n1), "E"))
        self.g.add_edge(HyperEdge((n1, n2, n5, n3, n4, n6), "S", rip=True))

        self.g.add_edge(HyperEdge((n2, n9), "E", boundary=True))
        self.g.add_edge(HyperEdge((n7, n10), "E"))
        self.g.add_edge(HyperEdge((n1, n11), "E"))
        # self.g.add_edge(HyperEdge((n1, n12), "E"))
        self.g.add_edge(HyperEdge((n12, n8), "E"))
        self.g.add_edge(HyperEdge((n6, n13), "E"))
        self.g.add_edge(HyperEdge((n4, n14), "E", boundary=True))

        self.g.add_edge(HyperEdge((n9, n10), "E", boundary=True))
        self.g.add_edge(HyperEdge((n10, n11), "E", boundary=True))
        self.g.add_edge(HyperEdge((n11, n12), "E", boundary=True))
        self.g.add_edge(HyperEdge((n12, n13), "E", boundary=True))
        self.g.add_edge(HyperEdge((n13, n14), "E", boundary=True))

        self.g.add_edge(HyperEdge((n10, n7, n2, n9), "Q", rip=True))
        self.g.add_edge(HyperEdge((n11, n1, n7, n10), "Q", rip=True))
        self.g.add_edge(HyperEdge((n12, n13, n6, n1), "Q", rip=True))
        self.g.add_edge(HyperEdge((n13, n14, n4, n6), "Q", rip=True))
        self.g.add_edge(HyperEdge((n11, n12, n8, n1), "Q", rip=True))

    def test_stage0(self):
        draw(self.g, "draw/test11-case7-stage0.png")

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 14)
        self.assertEqual(cnt.normal_hanging, 2)
        self.assertEqual(cnt.hyper_S, 1)
        self.assertEqual(cnt.hyper_S_rip, 1)
        self.assertEqual(cnt.hyper_Q, 5)
        self.assertEqual(cnt.hyper_Q_rip, 5)
        self.assertEqual(cnt.hyper_E, 19)
        self.assertEqual(cnt.hyper_E_boundary, 10)

    def test_stage1(self):
        applied = self.g.apply(self.p11)
        draw(self.g, "draw/test11-case7-stage1.png")
        self.assertEqual(applied, 1)

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 19)
        self.assertEqual(cnt.normal_hanging, 1)
        self.assertEqual(cnt.hyper_S, 6)
        self.assertEqual(cnt.hyper_S_rip, 0)
        self.assertEqual(cnt.hyper_Q, 5)
        self.assertEqual(cnt.hyper_Q_rip, 5)
        self.assertEqual(cnt.hyper_E, 29)
        self.assertEqual(cnt.hyper_E_boundary, 13)


if __name__ == '__main__':
    unittest.main()
