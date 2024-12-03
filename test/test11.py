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
        self.g.add_edge(HyperEdge((n1, n2, n5, n3, n4, n6), "Q", rip=True))

    def test_stage0(self):
        draw(self.g, "draw/test11-case1-stage0.png")

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 8)
        self.assertEqual(cnt.normal_hanging, 2)
        self.assertEqual(cnt.hyper_Q, 1)
        self.assertEqual(cnt.hyper_Q_rip, 1)
        self.assertEqual(cnt.hyper_E, 8)
        self.assertEqual(cnt.hyper_E_boundary, 0)

    def test_stage1(self):
        applied = self.g.apply(self.p11)
        draw(self.g, "draw/test11-case1-stage1.png")
        self.assertEqual(applied, 1)

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 13)
        self.assertEqual(cnt.normal_hanging, 4)
        self.assertEqual(cnt.hyper_Q, 6)
        self.assertEqual(cnt.hyper_Q_rip, 0)
        self.assertEqual(cnt.hyper_E, 18)
        self.assertEqual(cnt.hyper_E_boundary, 0)


if __name__ == '__main__':
    unittest.main()
