from graphtest import GraphTest
from node import Node
from edge import HyperEdge
from visualisation import draw
from productions.p1 import P1
import unittest

class TestP1Case1(unittest.TestCase):
    def setUp(self):
        # 4 --- E --- 3
        # |  \     /  |
        # E     Q     E
        # |  /     \  |
        # 1 --- E --- 2

        self.g = GraphTest()
        n1 = Node(0, 0, "n1")
        n2 = Node(1, 0, "n2")
        n3 = Node(1, 1, "n3")
        n4 = Node(0, 1, "n4")
        e1 = HyperEdge((n1, n2), "E", boundary=False)
        e3 = HyperEdge((n2, n3), "E", boundary=False)
        e4 = HyperEdge((n3, n4), "E", boundary=True)
        e2 = HyperEdge((n4, n1), "E", boundary=True)
        e5 = HyperEdge((n3, n4, n1, n2), "Q", rip=True)
        for n in [n1, n2, n3, n4]:
            self.g.add_node(n)
        for e in [e1, e2, e3, e4, e5]:
            self.g.add_edge(e)

        self.p1 = P1()

    def test_stage0(self):
        draw(self.g, "draw/test1-case1-stage0.png")

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 4)
        self.assertEqual(cnt.normal_hanging, 0)
        self.assertEqual(cnt.hyper, 5)
        self.assertEqual(cnt.hyper_Q, 1)
        self.assertEqual(cnt.hyper_Q_rip, 1)
        self.assertEqual(cnt.hyper_E, 4)
        self.assertEqual(cnt.hyper_E_boundary, 2)

    def test_stage1(self):
        self.g.apply(self.p1)
        draw(self.g, "draw/test1-case1-stage1.png")

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 9)
        self.assertEqual(cnt.normal_hanging, 2)
        self.assertEqual(cnt.hyper_Q, 4)
        self.assertEqual(cnt.hyper_Q_rip, 0)
        self.assertEqual(cnt.hyper_E, 12)
        self.assertEqual(cnt.hyper_E_boundary, 4)


class TestP1Case2(unittest.TestCase):
    def setUp(self):
        # 4 --- E --- 7 --- E --- 3
        # |  \     /  |  \     /  |
        # E     Q     E     Q     E
        # |  /     \  |  /     \  |
        # 8 --- E --- 9 --- E --- 6
        # |  \     /  |  \     /  |
        # E     Q     E     Q     E
        # |  /     \  |  /     \  |
        # 1 --- E --- 5 --- E --- 2

        self.g = GraphTest()
        n1 = Node(0, 0, "n1")
        n2 = Node(1, 0, "n2")
        n3 = Node(1, 1, "n3")
        n4 = Node(0, 1, "n4")
        n5 = Node(0.5, 0, "n5")
        n6 = Node(1, 0.5, "n6")
        n7 = Node(0.5, 1, "n7")
        n8 = Node(0, 0.5, "n8")
        n9 = Node(0.5, 0.5, "n9")
        for n in [n1, n2, n3, n4, n5, n6, n7, n8, n9]:
            self.g.add_node(n)

        # around the border
        self.g.add_edge(HyperEdge((n1, n5), "E", boundary=True))
        self.g.add_edge(HyperEdge((n5, n2), "E", boundary=True))
        self.g.add_edge(HyperEdge((n2, n6), "E", boundary=True))
        self.g.add_edge(HyperEdge((n6, n3), "E", boundary=True))
        self.g.add_edge(HyperEdge((n3, n7), "E", boundary=True))
        self.g.add_edge(HyperEdge((n7, n4), "E", boundary=True))
        self.g.add_edge(HyperEdge((n4, n8), "E", boundary=True))
        self.g.add_edge(HyperEdge((n8, n1), "E", boundary=True))

        # to center hyper-node
        self.g.add_edge(HyperEdge((n5, n9), "E"))
        self.g.add_edge(HyperEdge((n6, n9), "E"))
        self.g.add_edge(HyperEdge((n7, n9), "E"))
        self.g.add_edge(HyperEdge((n8, n9), "E"))

        # Q-tag hyper-nodes
        self.g.add_edge(HyperEdge((n1, n5, n9, n8), "Q", rip=True))
        self.g.add_edge(HyperEdge((n5, n2, n6, n9), "Q", rip=True))
        self.g.add_edge(HyperEdge((n8, n9, n7, n4), "Q", rip=True))
        self.g.add_edge(HyperEdge((n9, n6, n3, n7), "Q", rip=True))

        self.p1 = P1()

    def test_stage0(self):
        draw(self.g, "draw/test1-case2-stage0.png")

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 9)
        self.assertEqual(cnt.normal_hanging, 0)
        self.assertEqual(cnt.hyper_Q, 4)
        self.assertEqual(cnt.hyper_Q_rip, 4)
        self.assertEqual(cnt.hyper_E, 12)
        self.assertEqual(cnt.hyper_E_boundary, 8)

    def test_stage1(self):
        self.g.apply(self.p1)
        draw(self.g, "draw/test1-case2-stage1.png")

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 19)
        self.assertEqual(cnt.normal_hanging, 4)
        self.assertEqual(cnt.hyper_Q, 10)
        self.assertEqual(cnt.hyper_Q_rip, 2)
        self.assertEqual(cnt.hyper_E, 28)
        self.assertEqual(cnt.hyper_E_boundary, 12)


if __name__ == '__main__':
    unittest.main()