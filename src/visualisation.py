import networkx as nx
from graph import Graph, Attr
import matplotlib.pyplot as plt
import os


def create_directory(path):
    path = os.path.normpath(path)
    dir_path = os.path.dirname(path)
    if dir_path and not os.path.exists(dir_path):
        os.makedirs(dir_path)


def draw(g: Graph, filename: str = "test_draw.png") -> None:
    create_directory(filename)

    pos = {node: (node.x, node.y) for node in g.get_nodes()}
    pos_labels = {node: (x, y + 0.3) for node, (x, y) in pos.items()}
    labels = {
        node: f"{round(node.x,2 ), round(node.y,2)}" for node in g.get_nodes()}

    plt.figure(figsize=(12, 4))

    nx.draw_networkx_nodes(g.get_inner(), pos, node_size=2000,
                           edgecolors="black", linewidths=5,  alpha=0.5)
    nx.draw_networkx_edges(g.get_inner(), pos, width=5, alpha=0.3)
    nx.draw_networkx_labels(g.get_inner(), pos_labels, labels)

    ax = plt.gca()
    ax.margins(0.50)
    plt.axis("off")
    plt.savefig(filename)
    plt.cla()
    plt.clf()
