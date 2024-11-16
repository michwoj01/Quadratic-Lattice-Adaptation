from typing import List
import networkx as nx
from edge import Edge
from node import Node
from production import Production

class Attr:
    LVL = "level"
    LBL = "label"
    X = "x"
    Y = "y"

class Graph:

    def __init__(self):
        self._G = nx.Graph()

    def has_node(self, node: Node) -> bool:
        return node in self._G

    def has_edge(self, edge: Edge) -> bool:
        u, v = edge.nodes
        return self._G.has_edge(u, v)

    def add_node(self, node: Node) -> None:
        self._G.add_node(node)

    def get_nodes(self):
        return self._G.nodes
    
    def add_edge(self, edge: Edge):
        u, v = edge.nodes
        self._G.add_edge(u, v, hyperEdge=edge)

    def get_edges(self):
        return self._G.edges

    def get_edge(self, u: Node, v: Node) -> Edge:
        return self.get_edges()[u, v]['hyperEdge']

    def remove_node(self, node: Node):
        # also removes the edge
        self._G.remove_node(node)

    def remove_edge(self, edge: Edge):
        assert self.has_edge(edge)
        u, v = edge.nodes
        self._G.remove_edge(u, v)

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

    def get_node_neighbours(self, node: Node):
        return self._G.neighbors(node)
            
    def get_subgraph_on_nodes(self, nodes: List[Node]):
        return self._G.subgraph(nodes)

    def get(self, node: Node):
        # already exists
        return self._G[node]
        
    def copy(self):
        new_graph = Graph()
        new_graph._G = self._G.copy()
        return new_graph
    
    def get_data(self):
        xs = nx.get_node_attributes(self._G, Attr.X)
        ys = nx.get_node_attributes(self._G, Attr.Y)
        return xs, ys