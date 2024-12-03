from edge import HyperEdge
from graphtest import GraphTest
from node import Node
from edge import HyperEdge
from visualisation import draw
from productions.p6 import P6
import unittest

class TestP6Case1(unittest.TestCase):
    def setUp(self):
        self.g = GraphTest()

        n1 = Node(0, 0, "n1", hanging=False)
        n2 = Node(1, 0, "n2", hanging=False)
        n3 = Node(1, 1, "n3", hanging=False)
        n4 = Node(0, 1, "n4", hanging=False)
        n5 = Node(1, 0.5, "n5", hanging=True)
        n6 = Node(0.5, 0, "n6", hanging=True)
        n7 = Node(0, 0.5, "n7", hanging=True)
        n8 = Node(0.5, 1, "n8", hanging=True)
        for n in [n1, n2, n3, n4, n5, n6, n7, n8]:
            self.g.add_node(n)


        self.g.add_edge(HyperEdge((n1, n6), "E", boundary=True))
        self.g.add_edge(HyperEdge((n6, n2), "E", boundary=True))
        self.g.add_edge(HyperEdge((n2, n5), "E", boundary=True))
        self.g.add_edge(HyperEdge((n5, n3), "E", boundary=True))
        self.g.add_edge(HyperEdge((n3, n8), "E", boundary=True))
        self.g.add_edge(HyperEdge((n8, n4), "E", boundary=True))
        self.g.add_edge(HyperEdge((n4, n7), "E", boundary=True))
        self.g.add_edge(HyperEdge((n7, n1), "E", boundary=True))
        self.g.add_edge(HyperEdge((n3, n4, n1, n2), "Q", rip=True))
        self.p6 = P6()

    def test_stage0(self):
        draw(self.g, "draw/test6-case1-stage0.png")

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 8)
        self.assertEqual(cnt.normal_hanging, 4)
        self.assertEqual(cnt.hyper_Q, 1)
        self.assertEqual(cnt.hyper_Q_rip, 1)
        self.assertEqual(cnt.hyper_E, 8)
        self.assertEqual(cnt.hyper_E_boundary, 8)


    def test_stage1(self):
        applied = self.g.apply(self.p6)
        draw(self.g, "draw/test6-case1-stage1.png")
        self.assertEqual(applied, 1)

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 9)
        self.assertEqual(cnt.normal_hanging, 0)
        self.assertEqual(cnt.hyper_Q, 4)
        self.assertEqual(cnt.hyper_Q_rip, 0)
        self.assertEqual(cnt.hyper_E, 12)
        self.assertEqual(cnt.hyper_E_boundary, 8)


class TestP6Case2(unittest.TestCase):
    def setUp(self):
        self.p6 = P6()
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
        n25 = Node(0.5, 0, "n25")
        n26 = Node(0.5, 0.25, "n26", hanging=True)
        n27 = Node(1, 0.5, "n27")
        n28 = Node(0.75, 0.5, "n28", hanging=True)

        for n in [n0, n1, n2, n3, n4, n5, n6, n7, n10, n13, n14, n15, n16, n18, n19, n20, n21, n22, n23, n24, n25, n26, n27, n28]:
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
        self.g.add_edge(HyperEdge((n25, n26), "E"))
        
        self.g.add_edge(HyperEdge((n1, n25), "E", boundary=True))
        self.g.add_edge(HyperEdge((n25, n13), "E", boundary=True))
        self.g.add_edge(HyperEdge((n5, n27), "E", boundary=True))
        self.g.add_edge(HyperEdge((n14, n27), "E", boundary=True))
        self.g.add_edge(HyperEdge((n15, n28), "E"))
        self.g.add_edge(HyperEdge((n28, n7), "E"))
        self.g.add_edge(HyperEdge((n28, n27), "E"))
        self.g.add_edge(HyperEdge((n3, n26), "E"))
        self.g.add_edge(HyperEdge((n26, n15), "E"))
        self.g.add_edge(HyperEdge((n1, n25, n26, n3), "Q", rip=True))
        self.g.add_edge(HyperEdge((n25, n13, n15, n26), "Q", rip=True))
        self.g.add_edge(HyperEdge((n15, n14, n27, n28), "Q", rip=True))
        self.g.add_edge(HyperEdge((n28, n27, n5, n7), "Q", rip=True))
        self.g.add_edge(HyperEdge((n3, n15, n7, n24), "Q", rip=True))
    
    def test_stage0(self):
        draw(self.g, "draw/test6-case2-stage0.png")

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 24)
        self.assertEqual(cnt.normal_hanging, 4)
        self.assertEqual(cnt.hyper_Q, 13)
        self.assertEqual(cnt.hyper_Q_rip, 9)
        self.assertEqual(cnt.hyper_E, 36)
        self.assertEqual(cnt.hyper_E_boundary, 16)

    def test_stage1(self):
        applied = self.g.apply(self.p6)
        draw(self.g, "draw/test6-case2-stage1.png")
        self.assertEqual(applied, 1)

        cnt = self.g.count_nodes()
        self.assertEqual(cnt.normal, 25)
        self.assertEqual(cnt.normal_hanging, 0)
        self.assertEqual(cnt.hyper_Q, 16)
        self.assertEqual(cnt.hyper_Q_rip, 8)
        self.assertEqual(cnt.hyper_E, 40)
        self.assertEqual(cnt.hyper_E_boundary, 16)

if __name__ == '__main__':
    unittest.main()