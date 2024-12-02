from graphtest import GraphTest
from node import Node
from edge import HyperEdge
from visualisation import draw
from productions.p7 import P7
import unittest

class TestP7Case1(unittest.TestCase):
    def setUp(self):
        self.g = GraphTest()
        n1 = Node(0, 0, "n1")
        n2 = Node(1, 0, "n2")
        n3 = Node(1, 1, "n3")
        n4 = Node(0, 1, "n4")
        e1 = HyperEdge((n1, n2), "E", boundary=False)
        e3 = HyperEdge((n2, n3), "E", boundary=False)
        e4 = HyperEdge((n3, n4), "E", boundary=True)
        e2 = HyperEdge((n4, n1), "E", boundary=True)
        e5 = HyperEdge((n3, n4, n1, n2), "Q")
        for n in [n1, n2, n3, n4]:
            self.g.add_node(n)
        for e in [e1, e2, e3, e4, e5]:
            self.g.add_edge(e)

        self.p7 = P7()

    def test_stage0(self):
        draw(self.g, "draw/test7-case1-stage0.png")

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 4)
        self.assertEqual(cnt.normal_hanging, 0)
        self.assertEqual(cnt.hyper, 5)
        self.assertEqual(cnt.hyper_Q, 1)
        self.assertEqual(cnt.hyper_Q_rip, 0)
        self.assertEqual(cnt.hyper_E, 4)
        self.assertEqual(cnt.hyper_E_boundary, 2)

    def test_stage1(self):
        applied = self.g.apply(self.p7)
        draw(self.g, "draw/test7-case1-stage1.png")
        self.assertEqual(applied, 1)

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 4)
        self.assertEqual(cnt.normal_hanging, 0)
        self.assertEqual(cnt.hyper, 5)
        self.assertEqual(cnt.hyper_Q, 1)
        self.assertEqual(cnt.hyper_Q_rip, 1)
        self.assertEqual(cnt.hyper_E, 4)
        self.assertEqual(cnt.hyper_E_boundary, 2)

class TestP7Case2(unittest.TestCase):
    def setUp(self):
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

        self.p7 = P7()

    def test_stage0(self):
        draw(self.g, "draw/test7-case2-stage0.png")

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 4)
        self.assertEqual(cnt.normal_hanging, 0)
        self.assertEqual(cnt.hyper, 5)
        self.assertEqual(cnt.hyper_Q, 1)
        self.assertEqual(cnt.hyper_Q_rip, 1)
        self.assertEqual(cnt.hyper_E, 4)
        self.assertEqual(cnt.hyper_E_boundary, 2)

    def test_stage1(self):
        applied = self.g.apply(self.p7)
        draw(self.g, "draw/test7-case2-stage1.png")
        self.assertEqual(applied, 0)

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 4)
        self.assertEqual(cnt.normal_hanging, 0)
        self.assertEqual(cnt.hyper, 5)
        self.assertEqual(cnt.hyper_Q, 1)
        self.assertEqual(cnt.hyper_Q_rip, 1)
        self.assertEqual(cnt.hyper_E, 4)
        self.assertEqual(cnt.hyper_E_boundary, 2)

class TestP7Case3(unittest.TestCase):
    def setUp(self):
        self.g = GraphTest()
        n0 = Node(0, 0, "n0")
        n1 = Node(0.25, 0.0, "n1")
        n2 = Node(0.0, 0.25, "n2")
        n3 = Node(0.25, 0.25, "n3")
        n4 = Node(1, 1, "n4")
        n5 = Node(1.0, 0.75, "n5")
        n6 = Node(0.75, 1.0, "n6")
        n7 = Node(0.75, 0.75, "n7")
        n8 = Node(0.5, 0, "n8")
        n9 = Node(1, 0.5, "n9")
        n10 = Node(1, 0, "n10")
        n11 = Node(0.75, 0.5, "n11")
        n12 = Node(0.5, 0.25, "n12")
        n13 = Node(0.75, 0.0, "n13")
        n14 = Node(1.0, 0.25, "n14")
        n15 = Node(0.75, 0.25, "n15")
        n16 = Node(0, 0.5, "n16")
        n17 = Node(0.5, 0.5, "n17")
        n18 = Node(0.5, 1, "n18")
        n19 = Node(0, 1, "n19")
        n20 = Node(0.5, 0.75, "n20")
        n21 = Node(0.25, 0.5, "n21")
        n22 = Node(0.0, 0.75, "n22")
        n23 = Node(0.25, 1.0, "n23")
        n24 = Node(0.25, 0.75, "n24")

        for n in [n0, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15, n16, n17, n18, n19, n20, n21, n22, n23, n24]:
            self.g.add_node(n)

        self.g.add_edge(HyperEdge((n0, n1), "E", boundary=True))
        self.g.add_edge(HyperEdge((n1, n8), "E", boundary=True))
        self.g.add_edge(HyperEdge((n2, n16), "E", boundary=True))
        self.g.add_edge(HyperEdge((n0, n2), "E", boundary=True))
        self.g.add_edge(HyperEdge((n1, n3), "E"))
        self.g.add_edge(HyperEdge((n3, n12), "E"))
        self.g.add_edge(HyperEdge((n3, n21), "E"))
        self.g.add_edge(HyperEdge((n2, n3), "E"))
        self.g.add_edge(HyperEdge((n0, n1, n2, n3), "Q", rip=True))
        self.g.add_edge(HyperEdge((n1, n3, n8, n12), "Q", rip=True))
        self.g.add_edge(HyperEdge((n2, n3, n16, n21), "Q", rip=True))
        self.g.add_edge(HyperEdge((n3, n12, n17, n21), "Q", rip=True))
        self.g.add_edge(HyperEdge((n4, n5), "E", boundary=True))
        self.g.add_edge(HyperEdge((n5, n9), "E", boundary=True))
        self.g.add_edge(HyperEdge((n6, n18), "E", boundary=True))
        self.g.add_edge(HyperEdge((n4, n6), "E", boundary=True))
        self.g.add_edge(HyperEdge((n5, n7), "E"))
        self.g.add_edge(HyperEdge((n7, n11), "E"))
        self.g.add_edge(HyperEdge((n7, n20), "E"))
        self.g.add_edge(HyperEdge((n6, n7), "E"))
        self.g.add_edge(HyperEdge((n4, n5, n6, n7), "Q", rip=True))
        self.g.add_edge(HyperEdge((n5, n7, n9, n11), "Q", rip=True))
        self.g.add_edge(HyperEdge((n6, n7, n18, n20), "Q", rip=True))
        self.g.add_edge(HyperEdge((n7, n11, n17, n20), "Q", rip=True))
        self.g.add_edge(HyperEdge((n8, n12), "E"))
        self.g.add_edge(HyperEdge((n12, n17), "E"))
        self.g.add_edge(HyperEdge((n11, n17), "E"))
        self.g.add_edge(HyperEdge((n9, n11), "E"))
        self.g.add_edge(HyperEdge((n9, n14), "E", boundary=True))
        self.g.add_edge(HyperEdge((n10, n14), "E", boundary=True))
        self.g.add_edge(HyperEdge((n10, n13), "E", boundary=True))
        self.g.add_edge(HyperEdge((n8, n13), "E", boundary=True))
        self.g.add_edge(HyperEdge((n12, n15), "E"))
        self.g.add_edge(HyperEdge((n11, n15), "E"))
        self.g.add_edge(HyperEdge((n14, n15), "E"))
        self.g.add_edge(HyperEdge((n13, n15), "E"))
        self.g.add_edge(HyperEdge((n8, n12, n13, n15), "Q"))
        self.g.add_edge(HyperEdge((n11, n12, n15, n17), "Q"))
        self.g.add_edge(HyperEdge((n9, n11, n14, n15), "Q"))
        self.g.add_edge(HyperEdge((n10, n13, n14, n15), "Q"))
        self.g.add_edge(HyperEdge((n16, n21), "E"))
        self.g.add_edge(HyperEdge((n17, n21), "E"))
        self.g.add_edge(HyperEdge((n17, n20), "E"))
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
        self.g.add_edge(HyperEdge((n17, n20, n21, n24), "Q"))
        self.g.add_edge(HyperEdge((n18, n20, n23, n24), "Q"))
        self.g.add_edge(HyperEdge((n19, n22, n23, n24), "Q"))

        self.p7 = P7()

    def test_stage0(self):
        draw(self.g, "draw/test7-case3-stage0.png")

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 25)
        self.assertEqual(cnt.normal_hanging, 0)
        self.assertEqual(cnt.hyper, 56)
        self.assertEqual(cnt.hyper_Q, 16)
        self.assertEqual(cnt.hyper_Q_rip, 8)
        self.assertEqual(cnt.hyper_E, 40)
        self.assertEqual(cnt.hyper_E_boundary, 16)

    def test_stage1(self):
        applied = self.g.apply(self.p7)
        draw(self.g, "draw/test7-case3-stage1.png")
        self.assertEqual(applied, 8)

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 25)
        self.assertEqual(cnt.normal_hanging, 0)
        self.assertEqual(cnt.hyper, 56)
        self.assertEqual(cnt.hyper_Q, 16)
        self.assertEqual(cnt.hyper_Q_rip, 16)
        self.assertEqual(cnt.hyper_E, 40)
        self.assertEqual(cnt.hyper_E_boundary, 16)

if __name__ == '__main__':
    unittest.main()