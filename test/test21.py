
from edge import HyperEdge
from graphtest import GraphTest
from node import Node
from edge import HyperEdge
from visualisation import draw
from productions.p21 import P21
import math
import unittest


class TestP21Case1(unittest.TestCase):
    def setUp(self):
        self.g = GraphTest()

        n1 = Node(0.2,0 , "n1")
        n2 = Node(1, 0, "n2")
        n3 = Node(1, 1, "n3")
        n4 = Node(0.2, 1, "n4")
        n5 = Node(0, 0.5, "n5")
        n6 = Node(0.6, 0, "n6")

        for n in [n1, n2, n3, n4, n5, n6]:
            self.g.add_node(n)

        self.g.add_edge(HyperEdge((n3, n4, n1, n2, n5,n6), "Q", rip=False))
        
        self.p10= P21()

    def test_stage0(self):
        draw(self.g, "draw/test21-case1-stage0.png")

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 6)
        self.assertEqual(cnt.normal_hanging, 0)
        self.assertEqual(cnt.hyper, 1)
        self.assertEqual(cnt.hyper_Q, 1)
        self.assertEqual(cnt.hyper_Q_rip, 0)

    def test_stage1(self):
        applied = self.g.apply(self.p10)
        draw(self.g, "draw/test21-case1-stage1.png")
        self.assertEqual(applied, 1)

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 6)
        self.assertEqual(cnt.normal_hanging, 0)
        self.assertEqual(cnt.hyper, 1)
        self.assertEqual(cnt.hyper_Q, 1)
        self.assertEqual(cnt.hyper_Q_rip, 1)

if __name__ == '__main__':
    unittest.main()