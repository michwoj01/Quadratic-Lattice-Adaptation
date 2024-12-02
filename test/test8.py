from edge import HyperEdge
from graphtest import GraphTest
from node import Node
from edge import HyperEdge
from visualisation import draw
from productions.p8 import P8
import unittest

class TestP8Case1(unittest.TestCase):
    def setUp(self):
        # 4                   3           7
        #   \              /  |  \       /
        #    \            /   E    Q(R=1)
        #                     |  /       \
        #        Q(R=0)     5(h=1)        6
        #                     |
        #    /            \   E
        #   /              \  |
        # 1                   2

        self.g = GraphTest()

        n1 = Node(0, 0, "n1", hanging=False)
        n2 = Node(1, 0, "n2", hanging=False)
        n3 = Node(1, 1, "n3", hanging=False)
        n4 = Node(0, 1, "n4", hanging=True)
        n5 = Node(1, 0.5, "n5", hanging=True)
        n6 = Node(2, 0.5, "n6", hanging=False)
        n7 = Node(2, 1, "n7", hanging=False)
        for n in [n1, n2, n3, n4, n5, n6, n7]:
            self.g.add_node(n)

        e1 = HyperEdge((n2, n5), "E", boundary=False)
        e2 = HyperEdge((n5, n3), "E", boundary=False)
        e3 = HyperEdge((n3, n4, n1, n2), "Q", rip=False)
        e4 = HyperEdge((n7, n3, n5, n6), "Q", rip=True)
        for e in [e1, e2, e3, e4]:
            self.g.add_edge(e)

        self.p8 = P8()

    def test_stage0(self):
        draw(self.g, "draw/test8-case1-stage0.png")

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 7)
        self.assertEqual(cnt.normal_hanging, 2)
        self.assertEqual(cnt.hyper_Q, 2)
        self.assertEqual(cnt.hyper_Q_rip, 1)
        self.assertEqual(cnt.hyper_E, 2)
        self.assertEqual(cnt.hyper_E_boundary, 0)


    def test_stage1(self):
        applied = self.g.apply(self.p8)
        draw(self.g, "draw/test8-case1-stage1.png")
        self.assertEqual(applied, 1)

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 7)
        self.assertEqual(cnt.normal_hanging, 2)
        self.assertEqual(cnt.hyper_Q, 2)
        self.assertEqual(cnt.hyper_Q_rip, 2)
        self.assertEqual(cnt.hyper_E, 2)
        self.assertEqual(cnt.hyper_E_boundary, 0)


class TestP8Case2(unittest.TestCase):
    def setUp(self):
        # 4                   3            7 ---- \   / 10
        #   \              /  |  \       / E     Q(R=1)
        #    \            /   E    Q(R=0)  8(h=1) /   \ 9
        #                     |  /       \ E
        #        Q(R=0)     5(h=1)         6
        #                     |
        #    /            \   E
        #   /              \  |
        # 1                   2

        self.g = GraphTest()

        n1 = Node(0, 0, "n1", hanging=False)
        n2 = Node(1, 0, "n2", hanging=False)
        n3 = Node(1, 1, "n3", hanging=False)
        n4 = Node(0, 1, "n4", hanging=False)
        n5 = Node(1, 0.5, "n5", hanging=True)
        n6 = Node(2, 0.5, "n6", hanging=False)
        n7 = Node(2, 1, "n7", hanging=False)
        n8 = Node(2, 0.75, "n8", hanging=True)
        n9 = Node(3, 0.75, "n9", hanging=False)
        n10 = Node(3, 1, "n10", hanging=False)
        for n in [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]:
            self.g.add_node(n)

        e1 = HyperEdge((n2, n5), "E", boundary=False)
        e2 = HyperEdge((n5, n3), "E", boundary=False)

        e3 = HyperEdge((n7, n8), "E", boundary=False)
        e4 = HyperEdge((n8, n6), "E", boundary=False)
        
        e5 = HyperEdge((n3, n4, n1, n2), "Q", rip=False)
        e6 = HyperEdge((n7, n3, n5, n6), "Q", rip=False)
        e7 = HyperEdge((n8, n9, n10, n7), "Q", rip=True)
        for e in [e1, e2, e3, e4, e5, e6, e7]:
            self.g.add_edge(e)

        self.p8 = P8()

    def test_stage0(self):
        draw(self.g, "draw/test8-case2-stage0.png")

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 10)
        self.assertEqual(cnt.normal_hanging, 2)
        self.assertEqual(cnt.hyper_Q, 3)
        self.assertEqual(cnt.hyper_Q_rip, 1)
        self.assertEqual(cnt.hyper_E, 4)
        self.assertEqual(cnt.hyper_E_boundary, 0)

    def test_stage1(self):
        applied = self.g.apply(self.p8)
        draw(self.g, "draw/test8-case2-stage1.png")
        self.assertEqual(applied, 1)

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 10)
        self.assertEqual(cnt.normal_hanging, 2)
        self.assertEqual(cnt.hyper_Q, 3)
        self.assertEqual(cnt.hyper_Q_rip, 2)
        self.assertEqual(cnt.hyper_E, 4)
        self.assertEqual(cnt.hyper_E_boundary, 0)

    def test_stage2(self):
        applied1 = self.g.apply(self.p8)
        applied2 = self.g.apply(self.p8)
        draw(self.g, "draw/test8-case2-stage2.png")
        self.assertEqual(applied1, 1)
        self.assertEqual(applied2, 1)

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 10)
        self.assertEqual(cnt.normal_hanging, 2)
        self.assertEqual(cnt.hyper_Q, 3)
        self.assertEqual(cnt.hyper_Q_rip, 3)
        self.assertEqual(cnt.hyper_E, 4)
        self.assertEqual(cnt.hyper_E_boundary, 0)


if __name__ == '__main__':
    unittest.main()