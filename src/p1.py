from graph import Graph
from production import Production

@Production.register
class P1Example(Production):
    
    def check(self) -> bool:
        return True
    
    def apply(self, G: Graph) -> Graph:
        return Graph()