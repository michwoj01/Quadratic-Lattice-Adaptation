import networkx as nx
from graph import Graph, Attr
import matplotlib.pyplot as plt
import os

def create_directory(path):
    path = os.path.normpath(path)
    dir_path = os.path.dirname(path)
    if dir_path and not os.path.exists(dir_path):
        os.makedirs(dir_path)

def debug_print(g: Graph):
    print(g)
    for node in g.get_nodes():
        print(node, g.get(node))
    print("=" * 100)


def draw(g: Graph, filename: str = "test_draw.png") -> None:
    create_directory(filename)

    xs, ys = g.get_data()

    # create positions map for nodes
    pos = {node: (xs[node], ys[node]) for node in g.get_nodes()}

    # create labels for nodes by adding 0.3 to y coordinate
    pos_labels = {node: (x, y + 0.3) for node, (x, y) in pos.items()}

    labels = {node: f"{round(xs[node],2 ), round(ys[node],2)}" for node in g.get_nodes()}

    plt.figure(figsize=(12, 4))

    nx.draw_networkx_nodes(
        g,
        pos,
        node_size=2000,
        edgecolors="black",
        linewidths=5,
        alpha=0.5,
    )
    nx.draw_networkx_edges(g, pos, width=5, alpha=0.3)
    nx.draw_networkx_labels(g, pos_labels, labels)

    ax = plt.gca()
    ax.margins(0.20)
    plt.axis("off")
    plt.savefig(filename)
    plt.cla()
    plt.clf()


def save_graph_as_gephi(g: Graph, filename: str):
    graph = g.copy()
    create_directory(filename)
    for node in graph.get_nodes():
        graph.get(node)["node_type"] = graph.get(node)[Attr.LBL]
        graph.get(node)[Attr.X] += graph.get(node)[Attr.LVL] * 50
        graph.get(node)[Attr.Y] += graph.get(node)[Attr.LVL] * 50
    nx.write_gexf(graph, filename)
