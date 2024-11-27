from dataclasses import dataclass
from graph import Graph
from node import Node
from edge import HyperEdge

@dataclass
class NodeCount:
    normal = 0
    normal_hanging = 0
    hyper = 0
    hyper_Q = 0
    hyper_Q_rip = 0
    hyper_S = 0
    hyper_S_rip = 0
    hyper_E = 0
    hyper_E_boundary = 0
    hyper_unknown = 0

class GraphTest(Graph):
    def count_nodes(self) -> NodeCount:
        cnt = NodeCount()

        n: Node
        for n in self._G.nodes:
            if n.hyper:
                hr: HyperEdge = n.hyperref
                cnt.hyper += 1
                if hr.tag == "Q":
                    cnt.hyper_Q += 1
                    if hr.rip:
                        cnt.hyper_Q_rip += 1
                elif hr.tag == "S":
                    cnt.hyper_S += 1
                    if hr.rip:
                        cnt.hyper_S_rip += 1
                elif hr.tag == "E":
                    cnt.hyper_E += 1
                    if hr.boundary:
                        cnt.hyper_E_boundary += 1
                else:
                    cnt.hyper_unknown += 1
            else:
                cnt.normal += 1
                if n.hanging:
                    cnt.normal_hanging += 1

        return cnt