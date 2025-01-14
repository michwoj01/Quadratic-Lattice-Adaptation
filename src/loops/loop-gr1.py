from loops.starting_graph import get_starting_graph
from productions.p1 import P1
from productions.p10 import P10
from productions.p11 import P11
from productions.p12 import P12
from productions.p2 import P2
from productions.p21 import P21
from productions.p22 import P22
from productions.p3 import P3
from productions.p4 import P4
from productions.p5 import P5
from productions.p6 import P6
from productions.p8 import P8
from productions.p9 import P9
from visualisation import draw, draw_without_hyper

ITERATION = 0

g = get_starting_graph()

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

    all_failed = True

    while True:
        for prod in prods:
            while True:
                applied = g.apply(prod)
                print(applied, ITERATION)
                if applied != 0:
                    all_failed = False
                    draw(g, f"../draw/{ITERATION}-hyper.png")
                    draw_without_hyper(g, f"../draw/{ITERATION}.png")
                    ITERATION += 1
                else:
                    break
        if all_failed:
            break
        all_failed = True

# Pipeline

prods = [P1(), P2(), P3(), P4(), P5(), P6(), P8(), P9(), P10(), P11(), P12(), P22()]

apply_n_draw(P21())

apply_while(prods)

# instead of P7, we manually rip an edge
manual_rip_n_draw(4, 2)

apply_while(prods)

# instead of P7, we manually rip an edge
manual_rip_n_draw(4.75, 2)

apply_while(prods)