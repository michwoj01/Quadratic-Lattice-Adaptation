
from edge import HyperEdge
from graphtest import GraphTest
from node import Node
from edge import HyperEdge
from visualisation import draw
from productions.p10 import P10
import math
import unittest


class TestP10Case1(unittest.TestCase):
    def setUp(self):
        self.g = GraphTest()
        n1 = Node(0.25, 0, "n1")
        n2 = Node(0.75, 0, "n2")
        n3 = Node(0.75, 2*math.sqrt(0.25), "n3")
        n4 = Node(0.25, 2*math.sqrt(0.25), "n4")
        n5 = Node(1, math.sqrt(0.25), "n5")
        n6 = Node(0, math.sqrt(0.25), "n6")
        n7 = Node((n1.x+n2.x)/2, (n1.y+n2.y)/2, "n7", hanging=True)

        e1 = HyperEdge((n1, n7), "E")
        e2 = HyperEdge((n7, n2), "E")
        e3 = HyperEdge((n2, n5), "E")
        e4 = HyperEdge((n4, n3), "E")
        e5 = HyperEdge((n6, n4), "E")
        e6 = HyperEdge((n6, n1), "E")
        e7 = HyperEdge((n3, n5), "E")
        e8 = HyperEdge((n3, n4, n1, n2, n5 ,n6), "S", rip=True)
        for n in [n1, n2, n3, n4, n5, n6 , n7]:
            self.g.add_node(n)

        for e in [e1, e2, e3, e4, e5, e6, e7, e8]:
            self.g.add_edge(e)
        
        self.p10= P10()

    def test_stage0(self):
        draw(self.g, "draw/test10-case1-stage0.png")

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 7)
        self.assertEqual(cnt.normal_hanging, 1)
        self.assertEqual(cnt.hyper, 8)
        self.assertEqual(cnt.hyper_S, 1)
        self.assertEqual(cnt.hyper_S_rip, 1)
        self.assertEqual(cnt.hyper_E, 7)
        self.assertEqual(cnt.hyper_E_boundary, 0)

    def test_stage1(self):
        applied = self.g.apply(self.p10)
        draw(self.g, "draw/test10-case1-stage1.png")
        self.assertEqual(applied, 1)

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 13)
        self.assertEqual(cnt.normal_hanging, 5)
        self.assertEqual(cnt.hyper, 24)
        self.assertEqual(cnt.hyper_Q, 6)
        self.assertEqual(cnt.hyper_Q_rip, 0)
        self.assertEqual(cnt.hyper_E, 18)
        self.assertEqual(cnt.hyper_E_boundary, 0)



if __name__ == '__main__':
    unittest.main()