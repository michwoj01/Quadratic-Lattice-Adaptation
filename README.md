# Quadratic-Lattice-Adaptation
Recursive design of quadratic lattice adaptation in the course of Graph Grammars for
the winter semester 2024/2025 AGH University of Kraków.

## For Developers

Before you start coding, take some time to get familiar with the Graph class.
Stick to using its methods—don’t mess around with the internal networkx graph
directly. If you think the current API is missing something you need, feel free
to open a PR and suggest improvements.

### How Graph works

The Graph class is built on top of the networkx library, but there’s a twist: networkx
doesn’t support hyperedges, so we’re converting all hyper-edges to nodes. Only one interface
is exposed right now.

### Conventions
- This implementation uses node labels to uniquely identify them. All nodes should be
  created with indexes.
- Edges are created with `hypertag` parameter (E/Q/etc.) and the code automatically adds
  node labels to it.
- Nodes are enumerated counter-clockwise. Productions do not break previous indices and do a "second round"
  sometimes ending in the middle.
- **DON'T** use `src.` in imports. Configure your IDE properly. Python dictionaries are sensitive to class
  names...

## How to implement productions

Want to add a new production? Just create a file in the productions directory and
implement the Production interface. The interface tries to stay as close as possible to
mathematical representation of hyper-graphs productions. You define a left and right side.
Left side is matched against the whole graph and every match is replaced by your right side.

### Minimal exmaple

This example imports everything needes. Left side matches for any 2 nodes connected with `E`-type hyper-node.
Right side adds another `{lvl}-n3` node inbetween the matched nodes and connects to both `n1` and `n2` from left-side
with `E`-type hyper-node.

2 nodes and 1 node-hyper-edge are fetched from `left.ordered_nodes`. `boundary` attributes are copied to new hyper-nodes
and `hanging` is set to a negation of `boundary` of the original `hn1` node-hyper-edge from left-side.

```python
from edge import HyperEdge
from graph import Graph
from node import Node
from productions.production import Production

@Production.register
class P2Example(Production):
    def get_left_side(self) -> Graph:
        g = Graph()

        n1 = Node(0, 0, "n1")
        n2 = Node(0, 0, "n2")
        g.add_node(n1)
        g.add_node(n2)

        g.add_edge(HyperEdge((n1, n2), "E"))

        return g

    def get_right_side(self, left: Graph, lvl: int):
        # passed from above & updated with correct xy values
        n1, n2, hn1 = left.ordered_nodes
        g = Graph()

        n3 = Node((n1.x+n2.x)/2, (n1.y+n2.y)/2, f"{lvl}n3", hanging=not hn1.hyperref.boundary)
        g.add_node(n3)

        g.add_edge(HyperEdge((n1, n3), "E", boundary=hn1.hyperref.boundary))
        g.add_edge(HyperEdge((n2, n3), "E", boundary=hn1.hyperref.boundary))

        return g
```
