from edge import HyperEdge
from graphtest import GraphTest
from node import Node
from edge import HyperEdge
from visualisation import draw
from productions.p5 import P5
import unittest

class TestP5Case1(unittest.TestCase):
    def setUp(self):
        # 4(h=0)   --  E  --    3(h=0)
        # |  \                 /  |
        # E                       E
        # |                       |
        # 7(h=1)     Q(R=1)     5(h=1)
        # |                       |
        # E                       E
        # |  /                \   |
        # 1(h=0) -E- 6(h=1) -E- 2(h=0)
        self.g = GraphTest()
        n1 = Node(0, 0, "n1", hanging=False)
        n2 = Node(1, 0, "n2", hanging=False)
        n3 = Node(1, 1, "n3", hanging=False)
        n4 = Node(0, 1, "n4", hanging=False)
        n5 = Node(1, 0.5, "n5", hanging=True)
        n6 = Node(0.5, 0, "n6", hanging=True)
        n7 = Node(0, 0.5, "n7", hanging=True)
        for n in [n1, n2, n3, n4, n5, n6, n7]:
            self.g.add_node(n)


        self.g.add_edge(HyperEdge((n1, n6), "E", boundary=True))
        self.g.add_edge(HyperEdge((n6, n2), "E", boundary=True))
        self.g.add_edge(HyperEdge((n2, n5), "E", boundary=True))
        self.g.add_edge(HyperEdge((n5, n3), "E", boundary=True))
        self.g.add_edge(HyperEdge((n3, n4), "E", boundary=False))
        self.g.add_edge(HyperEdge((n4, n7), "E", boundary=True))
        self.g.add_edge(HyperEdge((n7, n1), "E", boundary=True))
        self.g.add_edge(HyperEdge((n3, n4, n1, n2), "Q", rip=True))
        self.p5 = P5()

    def test_stage0(self):
        draw(self.g, "draw/test5-case1-stage0.png")

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 7)
        self.assertEqual(cnt.normal_hanging, 3)
        self.assertEqual(cnt.hyper_Q, 1)
        self.assertEqual(cnt.hyper_Q_rip, 1)
        self.assertEqual(cnt.hyper_E, 7)
        self.assertEqual(cnt.hyper_E_boundary, 6)


    def test_stage1(self):
        applied = self.g.apply(self.p5)
        draw(self.g, "draw/test5-case1-stage1.png")
        self.assertEqual(applied, 1)

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 9)
        self.assertEqual(cnt.normal_hanging, 1)
        self.assertEqual(cnt.hyper_Q, 4)
        self.assertEqual(cnt.hyper_Q_rip, 0)
        self.assertEqual(cnt.hyper_E, 12)
        self.assertEqual(cnt.hyper_E_boundary, 6)

if __name__ == '__main__':
    unittest.main()