from application.dtos.minPathResume import MinPathResumeDto
from domain.graph import Graph
from application.dtos.findResume import FindResumeDto
import heapq

INF = -1
NOT_DEFINED = -2

class GraphFind:
  # Em alguns lugares temos o Id do vértice e não o Id do array
  # Essa função centraliza a lógica de converter de id normal para id de array
  def getArrayId(graphId: int):
    return graphId - 1

  # Implementação do algoritmo de Dijkstra para achar o menor caminho
  def Dijkstra(graph: Graph, origin: int) -> FindResumeDto:
    distances = [INF for _ in range(graph.numVertices)]
    predecessor = [[] for _ in range(graph.numVertices)]
    visited = [False for _ in range(graph.numVertices)]
    shortestPathsEdges = [[] for _ in range(graph.numVertices)]

    originId = GraphFind.getArrayId(origin)
    distances[originId] = 0

    # Heap que irá servir como fila de prioridade os vértices
    verticesToVisit = []
    heapq.heappush(verticesToVisit, (distances[originId], origin))

    # Enquanto tiver vértices na heap
    while len(verticesToVisit) > 0:
      # obtenho apenas o id do vértice
      current = heapq.heappop(verticesToVisit)[1]

      # Converto para o Id usado no array
      currentArrayId = GraphFind.getArrayId(current)
      
      # Se o vértice já foi visitado
      # segue para o próximo, pois
      # pode ser uma cópia com valor desatualizado
      if visited[currentArrayId]:
        continue
      
      # Se não foi visitado marca o vértice
      visited[currentArrayId] = True
      currentDistance = distances[currentArrayId]
      
      # Relaxar
      edges = graph.graph[current].items()
      # Para cada aresta 
      for id, edge in edges:
        # Pego o id de array do vértice que aquela aresta leva 
        destArrayId = GraphFind.getArrayId(edge.destination)
        weight = edge.weight

        # Se a distãncia é infinita ou maior do que o caminho que a aresta atual permite realizar
        if (distances[destArrayId] is INF) or (distances[destArrayId] > (currentDistance + weight)):
          # Atualizamos o peso
          distances[destArrayId] = currentDistance + weight
          # Atualizamos o antecessor
          predecessor[destArrayId] = [current]
          shortestPathsEdges[destArrayId] = [edge.id]
          # Adicionamos na heap
          heapq.heappush(verticesToVisit, (distances[destArrayId], edge.destination))
          continue
        
        # Se a distãncia é igual a que já foi encontrada
        # Adicionamos nos antecessores possíveis do respectivo vértice
        if distances[destArrayId] == (currentDistance + weight):
          predecessor[destArrayId].append(current)
          shortestPathsEdges[destArrayId].append(edge.id)
    
    return FindResumeDto(distances, predecessor, shortestPathsEdges)

  # Função para obter as arestas que compõem o subconjunto dos menores caminhos
  # e as arestas comuns a esses caminhos (caso existam)
  def getMinPathEdgesId(resume: FindResumeDto, origin: int, dest: int):
    minPathsEdges = set()
    commonEdges = GraphFind.getPaths(resume, dest, origin, minPathsEdges)

    return MinPathResumeDto(minPathsEdges, commonEdges)

  # Essa função recursivamente explora todos os caminhos a partir de um vértice de origem
  # para descobrir as arestas comuns a todos os caminhos
  # e no processo descobrir as areastas que compõem todos os caminhos
  # Obs.: Como a função é chamada após a execução do Dijkstra, ela 
  # explora o subconjunto dos menores caminhos do grafo original
  def getPaths(resume: FindResumeDto, current: int, origin: int, minPathsEdges: set):
    if current == origin:
      return set()
    
    currentId = GraphFind.getArrayId(current)
    commonEdges = set()
    first = True

    # Explora os antecessores do respectivo vértice
    for id, predecessor in enumerate(resume.predecessor[currentId]):
      edge = resume.shortestPathsEdges[currentId][id]
      minPathsEdges.add(edge)
      
      # Passo recursivo
      edgesPath = GraphFind.getPaths(resume, predecessor, origin, minPathsEdges)

      edgesPath.add(edge)

      if first:
        commonEdges = edgesPath
        first = False
      else:
        commonEdges = commonEdges.intersection(edgesPath)

    return commonEdges
    

