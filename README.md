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