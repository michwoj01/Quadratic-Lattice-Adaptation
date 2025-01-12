from graph import Graph
from node import Node
from productions.p1 import P1
from productions.p2 import P2
from productions.p3 import P3
from productions.p8 import P8
from visualisation import draw, draw_without_hyper
from edge import HyperEdge
from productions.p21 import P21
from productions.p9 import P9

ITERATION = 0

g = Graph()

# 12 nodes
n1 = Node(0, 0, "n1")
n2 = Node(6, 0, "n2")
n3 = Node(2, 1, "n3")
n4 = Node(4, 1, "n4")
n5 = Node(0, 2, "n5")
n6 = Node(1, 2, "n6")
n7 = Node(5, 2, "n7")
n8 = Node(6, 2, "n8")
n9 = Node(2, 3, "n9")
n10 = Node(4, 3, "n10")
n11 = Node(0, 4, "n11")
n12 = Node(6, 4, "n12")

for n in [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12]:
    g.add_node(n)

# border edges
e1 = HyperEdge((n1, n2), "E", boundary=True)
e2 = HyperEdge((n2, n8), "E", boundary=True)
e3 = HyperEdge((n8, n12), "E", boundary=True)
e4 = HyperEdge((n12, n11), "E", boundary=True)
e5 = HyperEdge((n11, n5), "E", boundary=True)
e6 = HyperEdge((n5, n1), "E", boundary=True)

for e in [e1, e2, e3, e4, e5, e6]:
    g.add_edge(e)

# inner edges

e7 = HyperEdge((n1, n3), "E")
e8 = HyperEdge((n3, n4), "E")
e9 = HyperEdge((n4, n2), "E")
e10 = HyperEdge((n5, n6), "E")
e11 = HyperEdge((n7, n8), "E")
e12 = HyperEdge((n6, n3), "E")
e13 = HyperEdge((n4, n7), "E")
e14 = HyperEdge((n7, n8), "E")
e15 = HyperEdge((n11, n9), "E")
e16 = HyperEdge((n9, n10), "E")
e17 = HyperEdge((n10, n12), "E")
e18 = HyperEdge((n6, n9), "E")
e19 = HyperEdge((n7, n10), "E")

for e in [e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19]:
    g.add_edge(e)

# q edges

q1 = HyperEdge((n1, n3, n4, n2), "Q")
q2 = HyperEdge((n1, n5, n6, n3), "Q")
q3 = HyperEdge((n2, n4, n7, n8), "Q")
q4 = HyperEdge((n5, n6, n9, n11), "Q")
q5 = HyperEdge((n7, n8, n10, n12), "Q")
q6 = HyperEdge((n11, n9, n10, n12), "Q")

for q in [q1, q2, q3, q4, q5, q6]:
    g.add_edge(q)

# S edges

s = HyperEdge((n3, n4, n7, n10, n9, n6), "S")

g.add_edge(s)

draw(g, "../draw/starting-hyper.png")
draw_without_hyper(g, "../draw/starting.png")

def apply_n_draw(prod):
    global ITERATION
    print(g.apply(prod), ITERATION)
    draw(g, f"../draw/{ITERATION}-hyper.png")
    draw_without_hyper(g, f"../draw/{ITERATION}.png")
    ITERATION += 1

def manual_rip_n_draw(x, y):
    global ITERATION
    g.rip_single_hyperedge(x, y)
    draw(g, f"../draw/{ITERATION}-hyper.png")
    draw_without_hyper(g, f"../draw/{ITERATION}.png")
    ITERATION += 1

def apply_while(prods):
    global ITERATION
    for prod in prods:
        while True:
            applied = g.apply(prod)
            print(applied, ITERATION)
            if applied == 0:
                break
        draw(g, f"../draw/{ITERATION}-hyper.png")
        draw_without_hyper(g, f"../draw/{ITERATION}.png")
        ITERATION += 1

# Pipeline

apply_n_draw(P21())

apply_n_draw(P9())

# instead of P7, we manually rip an edge
manual_rip_n_draw(4, 2)

apply_while([P8(), P2(), P3(), P1()])

# instead of P7, we manually rip an edge
manual_rip_n_draw(4.75, 2)

apply_while([P8(), P2(), P3(), P1()])