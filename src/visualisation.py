import networkx as nx
from graph import Graph
import matplotlib.pyplot as plt
import os


def create_directory(path):
    path = os.path.normpath(path)
    dir_path = os.path.dirname(path)
    if dir_path and not os.path.exists(dir_path):
        os.makedirs(dir_path)


def draw_nx_subgraph(g: Graph, gx: nx.Graph, hyper: bool) -> None:

    if hyper:
        shape = "s" # square
        size = 2000 # large
    else:
        shape = "o" # round
        size  = 200 # small

    pos = {node: (node.x, node.y) for node in gx.nodes()}
    nx.draw_networkx_nodes(
        gx, pos, edgecolors="black", linewidths=5, alpha=0.5,
        node_shape=shape,
        node_size=size
    )

    if hyper:
        # inside labels (node label)
        label_pos = {node: (x, y) for node, (x, y) in pos.items()}
        label_val = {node: node.get_display_label() for node in gx.nodes()}
        label_font = 20
    else:
        # outside labels (node label + position)
        label_pos = {node: (x, y + 0.05) for node, (x, y) in pos.items()}
        label_val = {node:  f"{node.get_display_label()}, h={1 if node.hanging else 0}\n" +
                            f"({node.x:4.2f}, {node.y:4.2f})" for node in gx.nodes()}
        label_font = 12

    nx.draw_networkx_labels(gx, label_pos, label_val, font_size=label_font)


def draw(g: Graph, filename: str = "test_draw.png"):
    create_directory(filename)
    plt.figure(figsize=(12, 12))

    gx: nx.Graph = g._G

    gx_normal = gx.subgraph(filter(lambda node: not node.hyper, gx))
    gx_hyper  = gx.subgraph(filter(lambda node:     node.hyper, gx))

    draw_nx_subgraph(g, gx_normal, False)
    draw_nx_subgraph(g, gx_hyper,  True)

    pos = {node: (node.x, node.y) for node in gx.nodes()}
    nx.draw_networkx_edges(gx, pos, width=5, alpha=0.3)

    ax = plt.gca()
    ax.margins(0.10)
    plt.tight_layout()
    plt.axis("off")
    plt.savefig(filename)
    plt.cla()
    plt.clf()
