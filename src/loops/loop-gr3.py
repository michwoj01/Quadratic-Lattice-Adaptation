from graphtest import GraphTest
from node import Node
from edge import HyperEdge
from visualisation import draw, draw_without_hyper

from productions.p1 import P1
from productions.p2 import P2
from productions.p3 import P3
from productions.p4 import P4
from productions.p5 import P5
from productions.p6 import P6
from productions.p8 import P8
from productions.p9 import P9
from productions.p10 import P10
from productions.p11 import P11
from productions.p12 import P12
from productions.p22 import P22Example

import unittest


class TestGroup3(unittest.TestCase):
    def manual_rip(self, x, y):
        self.g.rip_single_hyperedge(x, y)

    def apply_all_exhaustively(self):
        total_applied = 0
        applied = 1
        while applied > 0:
            applied = 0
            for prod_i, prod in enumerate(self.prods):
                curr_applied = self.g.apply(prod)
                if curr_applied > 0:
                    print(f'Applied P{self.prod_names[prod_i]} {curr_applied} time(s)')
                applied += curr_applied
            total_applied += applied

        return total_applied

    def setUp(self):
        self.prods = [P1(), P2(), P3(), P4(), P5(), P6(), P8(), P9(), P10(), P11(), P12(), P22Example()]
        self.prod_names = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 22]
        self.g = GraphTest()
        n1 = Node(0, 0, "n1")
        n2 = Node(1, 0, "n2")
        n3 = Node(1, 1, "n3")
        n4 = Node(0, 1, "n4")
        n5 = Node(0.25, 0.25, "n5")
        n6 = Node(0.75, 0.25, "n6")
        n7 = Node(0.85, 0.5, "n7")
        n8 = Node(0.75, 0.75, "n8")
        n9 = Node(0.25, 0.75, "n9")
        n10 = Node(0.15, 0.5, "n10")
        n11 = Node(1, 0.5, "n11")
        n12 = Node(0, 0.5, "n12")

        e1 = HyperEdge((n1, n2), "E", boundary=True)
        e2 = HyperEdge((n2, n11), "E", boundary=True)
        e3 = HyperEdge((n3, n11), "E", boundary=True)
        e4 = HyperEdge((n3, n4), "E", boundary=True)
        e5 = HyperEdge((n4, n12), "E", boundary=True)
        e6 = HyperEdge((n1, n12), "E", boundary=True)
        e7 = HyperEdge((n1, n5), "E", boundary=False)
        e8 = HyperEdge((n5, n6), "E", boundary=False)
        e9 = HyperEdge((n2, n6), "E", boundary=False)
        e10 = HyperEdge((n6, n7), "E", boundary=False)
        e11 = HyperEdge((n7, n11), "E", boundary=False)
        e12 = HyperEdge((n7, n8), "E", boundary=False)
        e13 = HyperEdge((n8, n9), "E", boundary=False)
        e14 = HyperEdge((n9, n10), "E", boundary=False)
        e15 = HyperEdge((n10, n12), "E", boundary=False)
        e16 = HyperEdge((n5, n10), "E", boundary=False)
        e17 = HyperEdge((n8, n3), "E", boundary=False)
        e18 = HyperEdge((n9, n4), "E", boundary=False)

        q1 = HyperEdge((n3, n4, n8, n9), "Q", rip=False)
        q2 = HyperEdge((n3, n11, n7, n8), "Q", rip=False)
        q3 = HyperEdge((n5, n6, n7, n8, n9, n10), "Q", rip=False)
        q4 = HyperEdge((n1, n5, n10, n12), "Q", rip=False)
        q5 = HyperEdge((n1, n2, n5, n6), "Q", rip=False)
        q6 = HyperEdge((n2, n6, n7, n11), "Q", rip=False)
        q7 = HyperEdge((n4, n9, n10, n12), "Q", rip=False)

        for n in [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12]:
            self.g.add_node(n)
        for e in [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18]:
            self.g.add_edge(e)
        for q in [q1, q2, q3, q4, q5, q6, q7]:
            self.g.add_edge(q)

    def test(self):
        draw(self.g, "../../test/draw/hyper_group3_stage0.png")
        draw_without_hyper(self.g, "../../test/draw/group3_stage0.png")

        self.manual_rip(0.90, 0.67)
        draw(self.g, "../../test/draw/hyper_group3_stage1.png")
        draw_without_hyper(self.g, "../../test/draw/group3_stage1.png")

        self.apply_all_exhaustively()
        draw(self.g, "../../test/draw/hyper_group3_stage2.png")
        draw_without_hyper(self.g, "../../test/draw/group3_stage2.png")

        self.manual_rip(0.85, 0.73)
        draw(self.g, "../../test/draw/hyper_group3_stage3.png")
        draw_without_hyper(self.g, "../../test/draw/group3_stage3.png")

        self.apply_all_exhaustively()
        draw(self.g, "../../test/draw/hyper_group3_stage4.png")
        draw_without_hyper(self.g, "../../test/draw/group3_stage4.png")

        # self.manual_rip(?, ?)
        # draw(self.g, "../../test/draw/hyper_group3_stage5.png")
        # draw_without_hyper(self.g, "../../test/draw/group3_stage5.png")




if __name__ == '__main__':
    unittest.main()
