from application.dtos.minPathResume import MinPathResumeDto
from domain.graph import Graph
from application.dtos.findResume import FindResumeDto
import heapq

INF = -1
NOT_DEFINED = -2

class GraphFind:
  def getArrayId(graphId: int):
    return graphId - 1

  def Dijkstra(graph: Graph, origin: int) -> FindResumeDto:
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
    
    return FindResumeDto(distances, predecessor, shortestPathsEdges)

  def getMinPathEdgesId(resume: FindResumeDto, origin: int, dest: int):
    minPathsEdges = set()
    minPaths = GraphFind.getPaths(resume, dest, origin, minPathsEdges)

    return MinPathResumeDto(minPathsEdges, minPaths)

  def getPaths(resume: FindResumeDto, current: int, origin: int, minPathsEdges: set):
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
    

