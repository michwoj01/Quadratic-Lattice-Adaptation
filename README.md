# Quadratic-Lattice-Adaptation
Recursive design of quadratic lattice adaptation in the course of Graph Grammars for the winter semester 2024/2025 AGH University of Kraków.

# For Developers

Before you start coding, take some time to get familiar with the Graph class. Stick to using its methods—don’t mess around with the internal networkx graph directly. If you think the current API is missing something you need, feel free to open a PR and suggest improvements.

# How Graph works

The Graph class is built on top of the networkx library, but there’s a twist: networkx doesn’t support hyperedges, so we’ve implemented them separately. That means you’ll find different methods for handling regular edges and hyperedges—don’t mix them up.

# How to implement productions

Want to add a new production? Just create a file in the productions directory and implement the Production interface. Here’s a quick example:

```python
from src.graph import Graph
from src.productions.production import Production


@Production.register
class P1Example(Production):
    # Example production that resets the graph

    def check(self, g: Graph) -> bool:
        return True

    def apply(self, g: Graph) -> Graph:
        return Graph()
```