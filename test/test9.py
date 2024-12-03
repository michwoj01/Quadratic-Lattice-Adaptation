
from edge import HyperEdge
from graphtest import GraphTest
from node import Node
from edge import HyperEdge
from visualisation import draw
from productions.p9 import P9
import math
import unittest


class TestP9Case1(unittest.TestCase):
    def setUp(self):
        self.g = GraphTest()
        n1 = Node(0.25, 0, "n1")
        n2 = Node(0.75, 0, "n2")
        n3 = Node(0.75, 2*math.sqrt(0.25), "n3")
        n4 = Node(0.25, 2*math.sqrt(0.25), "n4")
        n5 = Node(1, math.sqrt(0.25), "n5")
        n6 = Node(0, math.sqrt(0.25), "n6")

        e1 = HyperEdge((n1, n2), "E")
        e2 = HyperEdge((n2, n5), "E")
        e3 = HyperEdge((n4, n3), "E")
        e4 = HyperEdge((n6, n4), "E")
        e5 = HyperEdge((n6, n1), "E")
        e6 = HyperEdge((n3, n5), "E")
        e7 = HyperEdge((n3, n4, n1, n2, n5 ,n6), "S", rip=True)
        for n in [n1, n2, n3, n4, n5, n6]:
            self.g.add_node(n)

        for e in [e1, e2, e3, e4, e5, e6, e7]:
            self.g.add_edge(e)
        
        self.p9= P9()

    def test_stage0(self):
        draw(self.g, "draw/test9-case1-stage0.png")

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 6)
        self.assertEqual(cnt.normal_hanging, 0)
        self.assertEqual(cnt.hyper, 7)
        self.assertEqual(cnt.hyper_S, 1)
        self.assertEqual(cnt.hyper_S_rip, 1)
        self.assertEqual(cnt.hyper_E, 6)
        self.assertEqual(cnt.hyper_E_boundary, 0)

    def test_stage1(self):
        applied = self.g.apply(self.p9)
        draw(self.g, "draw/test9-case1-stage1.png")
        self.assertEqual(applied, 1)

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 13)
        self.assertEqual(cnt.normal_hanging, 6)
        self.assertEqual(cnt.hyper, 24)
        self.assertEqual(cnt.hyper_Q, 6)
        self.assertEqual(cnt.hyper_Q_rip, 0)
        self.assertEqual(cnt.hyper_E, 18)
        self.assertEqual(cnt.hyper_E_boundary, 0)

# 2 TEST - HyperEdge S, R=0 - production not applied
class TestP9Case2(unittest.TestCase):
    def setUp(self):
        self.g = GraphTest()
        n1 = Node(0.25, 0, "n1")
        n2 = Node(0.75, 0, "n2")
        n3 = Node(0.75, 2*math.sqrt(0.25), "n3")
        n4 = Node(0.25, 2*math.sqrt(0.25), "n4")
        n5 = Node(1, math.sqrt(0.25), "n5")
        n6 = Node(0, math.sqrt(0.25), "n6")

        e1 = HyperEdge((n1, n2), "E")
        e2 = HyperEdge((n2, n5), "E")
        e3 = HyperEdge((n4, n3), "E")
        e4 = HyperEdge((n6, n4), "E")
        e5 = HyperEdge((n6, n1), "E")
        e6 = HyperEdge((n3, n5), "E")
        e7 = HyperEdge((n3, n4, n1, n2, n5 ,n6), "S", rip=False)
        for n in [n1, n2, n3, n4, n5, n6]:
            self.g.add_node(n)

        for e in [e1, e2, e3, e4, e5, e6, e7]:
            self.g.add_edge(e)
        
        self.p9= P9()

    def test_stage0(self):
        draw(self.g, "draw/test9-case2-stage0.png")

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 6)
        self.assertEqual(cnt.normal_hanging, 0)
        self.assertEqual(cnt.hyper, 7)
        self.assertEqual(cnt.hyper_S, 1)
        self.assertEqual(cnt.hyper_S_rip, 0)
        self.assertEqual(cnt.hyper_E, 6)
        self.assertEqual(cnt.hyper_E_boundary, 0)

    def test_stage1(self):
        applied = self.g.apply(self.p9)
        draw(self.g, "draw/test9-case2-stage1.png")
        self.assertEqual(applied, 0)

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 6)
        self.assertEqual(cnt.normal_hanging, 0)
        self.assertEqual(cnt.hyper, 7)
        self.assertEqual(cnt.hyper_S, 1)
        self.assertEqual(cnt.hyper_S_rip, 0)
        self.assertEqual(cnt.hyper_E, 6)
        self.assertEqual(cnt.hyper_E_boundary, 0) 

# TEST 3 - bigger graph
class TestP9Case3(unittest.TestCase):
    def setUp(self):
        self.g = GraphTest()
        n1 = Node(0.25, 0, "n1")
        n2 = Node(0.75, 0, "n2")
        n3 = Node(0.75, 2*math.sqrt(0.25), "n3")
        n4 = Node(0.25, 2*math.sqrt(0.25), "n4")
        n5 = Node(1, math.sqrt(0.25), "n5")
        n6 = Node(0, math.sqrt(0.25), "n6")
        n7 = Node(1, 0, "n7")
        n8 = Node(1.5, math.sqrt(0.25), "n8")
        n9 = Node(1, 2*math.sqrt(0.25), "n9")


        e1 = HyperEdge((n1, n2), "E")
        e2 = HyperEdge((n2, n5), "E")
        e3 = HyperEdge((n4, n3), "E")
        e4 = HyperEdge((n6, n4), "E")
        e5 = HyperEdge((n6, n1), "E")
        e6 = HyperEdge((n3, n5), "E")
        e7 = HyperEdge((n3, n4, n1, n2, n5 ,n6), "S", rip=True)
        e8 = HyperEdge((n7, n8), "E")
        e9 = HyperEdge((n8, n9), "E")
        e10 = HyperEdge((n9, n3), "E")
        e11 = HyperEdge((n7, n2), "E")
        e12 = HyperEdge((n8, n5), "E")

        for n in [n1, n2, n3, n4, n5, n6, n7, n8 ,n9]:
            self.g.add_node(n)

        for e in [e1, e2, e3, e4, e5, e6, e7, e8 ,e9, e10, e11, e12]:
            self.g.add_edge(e)

        self.p9= P9()

    def test_stage0(self):
        draw(self.g, "draw/test9-case3-stage0.png")

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 9)
        self.assertEqual(cnt.normal_hanging, 0)
        self.assertEqual(cnt.hyper, 12)
        self.assertEqual(cnt.hyper_S, 1)
        self.assertEqual(cnt.hyper_S_rip, 1)
        self.assertEqual(cnt.hyper_E, 11)
        self.assertEqual(cnt.hyper_E_boundary, 0)

    def test_stage1(self):
        applied = self.g.apply(self.p9)
        draw(self.g, "draw/test9-case3-stage1.png")
        self.assertEqual(applied, 1)

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 16)
        self.assertEqual(cnt.normal_hanging, 6)
        self.assertEqual(cnt.hyper, 29)
        self.assertEqual(cnt.hyper_Q, 6)
        self.assertEqual(cnt.hyper_Q_rip, 0)
        self.assertEqual(cnt.hyper_E, 23)
        self.assertEqual(cnt.hyper_E_boundary, 0)

if __name__ == '__main__':
    unittest.main()