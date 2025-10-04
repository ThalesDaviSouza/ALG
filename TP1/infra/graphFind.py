from domain.edge import Edge
from domain.graph import Graph
import heapq

INF = -1
SEM_ANTECESSOR = -2

class Resumo:
  def __init__(self, distances, predecessor):
    self.distances = distances
    self.predecessor = predecessor

class GraphFind:
  def getArrayId(graphId: int):
    return graphId - 1

  def Dijkstra(graph: Graph, origin: int) -> Resumo:
    distances = [INF for _ in range(graph.numVertices)]
    predecessor = [SEM_ANTECESSOR for _ in range(graph.numVertices)]
    visited = [False for _ in range(graph.numVertices)]

    originId = GraphFind.getArrayId(origin)
    distances[originId] = 0

    verticesToVisit = []
    heapq.heappush(verticesToVisit, (distances[originId], origin))

    while len(verticesToVisit) > 0:
      # obtenho apenas o id do vértice
      current = heapq.heappop(verticesToVisit)[1]

      currentArrayId = GraphFind.getArrayId(current)
      
      # se o vértice já foi visitado
      # segue para o próximo, pois
      # pode ser uma cópia com valor desatualizado
      if visited[currentArrayId]:
        continue

      visited[currentArrayId] = True
      currentDistance = distances[currentArrayId]
      
      # relaxar
      edges = graph.graph[current].items()
      for id, edge in edges:
        destArrayId = GraphFind.getArrayId(edge.destination)
        weight = edge.weight

        if (distances[destArrayId] is INF) or (distances[destArrayId] > (currentDistance + weight)):
          distances[destArrayId] = currentDistance + weight
          predecessor[destArrayId] = current
          heapq.heappush(verticesToVisit, (distances[destArrayId], edge.destination))
          continue

        if distances[destArrayId] == (currentDistance + weight):
          print('uma aresta com peso igual')
    
    return Resumo(distances, predecessor)
