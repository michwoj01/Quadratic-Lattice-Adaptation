from typing import List
import networkx as nx
from edge import Edge, HyperEdge
from node import Node
from src.productions.production import Production


class Attr:
    LVL = "level"
    LBL = "label"
    X = "x"
    Y = "y"


class Graph:

    def __init__(self):
        self._G = nx.Graph()
        self._hyperEdges = set()

    def has_node(self, node: Node) -> bool:
        return node in self._G

    def has_edge(self, edge: Edge) -> bool:
        u, v = edge.nodes
        return self._G.has_edge(u, v)

    def has_hyperEdge(self, hyperEdge: HyperEdge) -> bool:
        return hyperEdge in self._hyperEdges

    def add_node(self, node: Node) -> None:
        assert not self.has_node(node)
        self._G.add_node(node)

    def get_nodes(self) -> List[Node]:
        return self._G.nodes

    def add_hyperEdge(self, hyperEdge: HyperEdge):
        assert not self.has_hyperEdge(hyperEdge)
        self._hyperEdges.add(hyperEdge)

    def add_edge(self, edge: Edge):
        assert not self.has_edge(edge)
        u, v = edge.nodes
        self._G.add_edge(u, v, hyperEdge=edge)

    def get_edges(self):
        edges = []
        for u, v, data in self._G.edges(data=True):
            edge = data["hyperEdge"]
            edges.append(edge)
        return edges

    def get_edge(self, u: Node, v: Node) -> Edge:
        return self.get_edges()[u, v]["hyperEdge"]

    def get_hyperEdges(self):
        return self._hyperEdges

    def remove_node(self, node: Node):
        # also removes the edge attached to this node
        self._G.remove_node(node)

    def remove_edge(self, edge: Edge):
        assert self.has_edge(edge)
        u, v = edge.nodes
        self._G.remove_edge(u, v)

    def remove_hyperEdge(self, hyperEdge: HyperEdge):
        assert self.has_hyperEdge(hyperEdge)
        self._hyperEdges.remove(hyperEdge)

    def replace_node(self, old_node: Node, new_node: Node):
        assert self.has_node(old_node)
        self._G.add_node(new_node)
        for neighbor in self.get_node_neighbours(old_node):
            old_edge = self.get_edge(old_node, neighbor)
            new_edge = old_edge.copy_with_different_point(neighbor, new_node)
            self.add_edge(new_edge)
        self._G.remove_node(old_node)

    def replace_edge(self, new_edge: Edge):
        self.remove_edge(new_edge)
        self.add_edge(new_edge)

    # todo - use production
    def apply(self, production: Production):
        assert production.check(self)
        return production.apply(self)

    def check_if_production_possible(self, production: Production):
        return production.check(self)

    def get_node_neighbours(self, node: Node):
        return self._G.neighbors(node)

    def get_subgraph_on_nodes(self, nodes: List[Node]):
        return self._G.subgraph(nodes)

    def copy(self):
        new_graph = Graph()
        new_graph._G = self._G.copy()
        new_graph._hyperEdges = self._hyperEdges.copy()
        return new_graph

    def get_inner(self):
        return self._G

    def __convert_hyperEdges_to_edges(self):
        for hyperEdge in self.get_hyperEdges():
            nodes = hyperEdge.nodes
            x = sum([node.x for node in nodes]) / len(nodes)
            y = sum([node.y for node in nodes]) / len(nodes)
            new_node = Node(x, y, False)
            self.add_node(new_node)
            for node in nodes:
                self.add_edge(Edge((new_node, node), "E", False, False))
        self._hyperEdges = set()

    def get_visual_representation(self):
        new_g = self.copy()
        new_g.__convert_hyperEdges_to_edges()
        return new_g
