from domain.edge import Edge

class Graph:
  def __init__(self):
    self.graph = {} # lista de adjacencia
    self.numVertices = 0
    self.numEdges = 0

  # Lógica de adiconar uma aresta no grafo (não direcionado)
  def addEdge(self, id: int, origin: int, dest: int, weight: int):   
    if origin not in self.graph:
      self.graph[origin] = {}
    
    if dest not in self.graph:
      self.graph[dest] = {}
    
    self.graph[origin][dest] = Edge(id, dest, weight)
    self.graph[dest][origin] = Edge(id, origin, weight)

  # Lógica de recuperar uma aresta do grafo
  def getEdge(self, origin: int, dest: int):
    if origin not in self.graph:
      return None
    if dest not in self.graph[origin]:
      return None

    return self.graph[origin][dest]