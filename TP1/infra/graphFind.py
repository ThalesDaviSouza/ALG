from domain.edge import Edge
from domain.graph import Graph
import heapq

INF = -1
NOT_DEFINED = -2

class FindResume:
  def __init__(self, distances, predecessor: list[list], shortestPathsEdges):
    self.distances = distances
    self.predecessor = predecessor
    self.shortestPathsEdges = shortestPathsEdges

class GraphFind:
  def getArrayId(graphId: int):
    return graphId - 1

  def Dijkstra(graph: Graph, origin: int) -> FindResume:
    distances = [INF for _ in range(graph.numVertices)]
    predecessor = [[] for _ in range(graph.numVertices)]
    visited = [False for _ in range(graph.numVertices)]
    shortestPathsEdges = [[] for _ in range(graph.numVertices)]

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
          predecessor[destArrayId] = [current]
          shortestPathsEdges[destArrayId] = [edge.id]
          heapq.heappush(verticesToVisit, (distances[destArrayId], edge.destination))
          continue

        if distances[destArrayId] == (currentDistance + weight):
          predecessor[destArrayId].append(current)
          shortestPathsEdges[destArrayId].append(edge.id)
    
    return FindResume(distances, predecessor, shortestPathsEdges)

  def getMinPathEdgesId(resume: FindResume, origin: int, dest: int):
    minPathsEdges = set()
    minPaths = GraphFind.getPaths(resume, dest, origin, minPathsEdges)

    print(f'minPathsEdges: {minPathsEdges}')
    print(f'minPaths: {minPaths}')

  def getPaths(resume: FindResume, current: int, origin: int, minPathsEdges: set):
    if current == origin:
      return set()
    
    currentId = GraphFind.getArrayId(current)
    commonEdges = set()
    first = True

    for id, predecessor in enumerate(resume.predecessor[currentId]):
      edge = resume.shortestPathsEdges[currentId][id]
      minPathsEdges.add(edge)
      edgesPath = GraphFind.getPaths(resume, predecessor, origin, minPathsEdges)
      edgesPath.add(edge)

      if first:
        commonEdges = edgesPath
        first = False
      else:
        commonEdges = commonEdges.intersection(edgesPath)

    return commonEdges
    

