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


class TestP8Case3(unittest.TestCase):
    def setUp(self):
        self.p8 = P8()
        self.g = GraphTest()
        n0 = Node(0, 0, "n0")
        n1 = Node(0.25, 0.0, "n1")
        n2 = Node(0.0, 0.25, "n2")
        n3 = Node(0.25, 0.25, "n3")
        n4 = Node(1, 1, "n4")
        n5 = Node(1.0, 0.75, "n5")
        n6 = Node(0.75, 1.0, "n6")
        n7 = Node(0.75, 0.75, "n7")
        n10 = Node(1, 0, "n10")
        n13 = Node(0.75, 0.0, "n13")
        n14 = Node(1.0, 0.25, "n14")
        n15 = Node(0.75, 0.25, "n15")
        n16 = Node(0, 0.5, "n16")
        n18 = Node(0.5, 1, "n18")
        n19 = Node(0, 1, "n19")
        n20 = Node(0.5, 0.75, "n20", hanging=True)
        n21 = Node(0.25, 0.5, "n21", hanging=True)
        n22 = Node(0.0, 0.75, "n22")
        n23 = Node(0.25, 1.0, "n23")
        n24 = Node(0.25, 0.75, "n24")

        for n in [n0, n1, n2, n3, n4, n5, n6, n7, n10, n13, n14, n15, n16, n18, n19, n20, n21, n22, n23, n24]:
            self.g.add_node(n)

        self.g.add_edge(HyperEdge((n0, n1), "E", boundary=True))
        self.g.add_edge(HyperEdge((n2, n16), "E", boundary=True))
        self.g.add_edge(HyperEdge((n0, n2), "E", boundary=True))
        self.g.add_edge(HyperEdge((n1, n3), "E"))
        self.g.add_edge(HyperEdge((n3, n21), "E"))
        self.g.add_edge(HyperEdge((n2, n3), "E"))
        self.g.add_edge(HyperEdge((n0, n1, n2, n3), "Q", rip=True))
        self.g.add_edge(HyperEdge((n2, n3, n16, n21), "Q", rip=True))
        self.g.add_edge(HyperEdge((n4, n5), "E", boundary=True))
        self.g.add_edge(HyperEdge((n6, n18), "E", boundary=True))
        self.g.add_edge(HyperEdge((n4, n6), "E", boundary=True))
        self.g.add_edge(HyperEdge((n5, n7), "E"))
        self.g.add_edge(HyperEdge((n7, n20), "E"))
        self.g.add_edge(HyperEdge((n6, n7), "E"))
        self.g.add_edge(HyperEdge((n4, n5, n6, n7), "Q", rip=True))
        self.g.add_edge(HyperEdge((n6, n7, n18, n20), "Q", rip=True))
        self.g.add_edge(HyperEdge((n10, n14), "E", boundary=True))
        self.g.add_edge(HyperEdge((n10, n13), "E", boundary=True))
        self.g.add_edge(HyperEdge((n14, n15), "E"))
        self.g.add_edge(HyperEdge((n13, n15), "E"))
        self.g.add_edge(HyperEdge((n10, n13, n14, n15), "Q"))
        self.g.add_edge(HyperEdge((n16, n21), "E"))
        self.g.add_edge(HyperEdge((n18, n20), "E"))
        self.g.add_edge(HyperEdge((n18, n23), "E", boundary=True))
        self.g.add_edge(HyperEdge((n19, n23), "E", boundary=True))
        self.g.add_edge(HyperEdge((n19, n22), "E", boundary=True))
        self.g.add_edge(HyperEdge((n16, n22), "E", boundary=True))
        self.g.add_edge(HyperEdge((n21, n24), "E"))
        self.g.add_edge(HyperEdge((n20, n24), "E"))
        self.g.add_edge(HyperEdge((n23, n24), "E"))
        self.g.add_edge(HyperEdge((n22, n24), "E"))
        self.g.add_edge(HyperEdge((n16, n21, n22, n24), "Q"))
        self.g.add_edge(HyperEdge((n18, n20, n23, n24), "Q"))
        self.g.add_edge(HyperEdge((n19, n22, n23, n24), "Q"))

        self.g.add_edge(HyperEdge((n1, n13), "E", boundary=True))
        self.g.add_edge(HyperEdge((n5, n14), "E", boundary=True))
        self.g.add_edge(HyperEdge((n3, n15), "E"))
        self.g.add_edge(HyperEdge((n7, n15), "E"))
        self.g.add_edge(HyperEdge((n1, n13, n15, n3), "Q", rip=True))
        self.g.add_edge(HyperEdge((n15, n14, n5, n7), "Q", rip=True))
        self.g.add_edge(HyperEdge((n3, n15, n7, n24), "Q", rip=False))

    def test_stage0(self):
        draw(self.g, "draw/test8-case3-stage0.png")

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 20)
        self.assertEqual(cnt.normal_hanging, 2)
        self.assertEqual(cnt.hyper_Q, 11)
        self.assertEqual(cnt.hyper_Q_rip, 6)
        self.assertEqual(cnt.hyper_E, 30)
        self.assertEqual(cnt.hyper_E_boundary, 14)

    def test_stage1(self):
        applied = self.g.apply(self.p8)
        draw(self.g, "draw/test8-case3-stage1.png")
        self.assertEqual(applied, 1)

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 20)
        self.assertEqual(cnt.normal_hanging, 2)
        self.assertEqual(cnt.hyper_Q, 11)
        self.assertEqual(cnt.hyper_Q_rip, 7)
        self.assertEqual(cnt.hyper_E, 30)
        self.assertEqual(cnt.hyper_E_boundary, 14)


if __name__ == '__main__':
    unittest.main()
