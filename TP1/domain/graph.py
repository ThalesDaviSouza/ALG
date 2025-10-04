from domain.edge import Edge

class Graph:
  def __init__(self):
    # lista de adjacencia
    self.graph = {}
    self.numVertices = 0
    self.numEdges = 0

  def addEdge(self, origin: int, dest: int, weight: int):   
    if origin not in self.graph:
      self.graph[origin] = {}
    
    if dest not in self.graph:
      self.graph[dest] = {}
    
    self.graph[origin][dest] = Edge(dest, weight)
    self.graph[dest][origin] = Edge(origin, weight)

  def getEdge(self, origin: int, dest: int) -> None | Edge:
    if origin not in self.graph:
      return None
    if dest not in self.graph[origin]:
      return None

    return self.graph[origin][dest]