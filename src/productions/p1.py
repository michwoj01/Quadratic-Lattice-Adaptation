from src.graph import Graph
from src.productions.production import Production


@Production.register
class P1Example(Production):
    # Example: A production that resets the graph

    def check(self, g: Graph) -> bool:
        # Check if the production can be applied
        return True

    def apply(self, g: Graph) -> Graph:
        # Apply the production (in this case, reset the graph)
        return Graph()
