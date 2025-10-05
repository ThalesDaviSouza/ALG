from application.dtos.findResume import FindResumeDto
from application.dtos.minPathResume import MinPathResumeDto
from domain.graph import Graph
from infra.graphFind import GraphFind

class Logger:
  # Função para imprimir um grafo (para fins de teste)
  def logGraph(graph: Graph):
    print('Grafo:')
    for id in sorted(graph.graph.keys()):
      edgesIds = graph.graph[id].keys()
      edges_str = ', '.join(str(graph.graph[id][edgeId]) for edgeId in edgesIds)
      print(f'{id} -> [{edges_str}]')
  
  # Função para imprimir o resumo da busca (para fins de teste)
  def logFindResume(resume: FindResumeDto):
    print(f'{resume.distances}: distances')
    print(f'{resume.predecessor}: predecessor')
    print(f'{resume.shortestPathsEdges}: shortestPathsEdges')

  # Função para imprimir a dístância do menor caminho para o vértice X
  # Se refere a primeira parte do trabalho
  def logMinPathLength(resume: FindResumeDto, dest: int):
    destId = GraphFind.getArrayId(dest)
    print(f'Parte 1: {resume.distances[destId]}')
  
  # Função para imprimir os ids das arestas que compõem o subconjunto dos menores caminhos
  # do vértice 1 até o vértice N
  # Obs.: Os ids são imprimidos em ordem crescente
  def logMinPathEdgesId(resume: MinPathResumeDto):
    minPathsEdges = sorted(resume.minPathsEdges)
    edgesIdStr = ' '.join(str(edgeId) for edgeId in minPathsEdges)
    print(f'Parte 2: {edgesIdStr}')
  
  # Função para imprimir os ids das arestas críticas do vértice 1 até o vértice N
  # Obs.: Os ids são imprimidos em ordem crescente
  # É imprimido -1 caso não tenha arestas críticas
  def logCriticalEdges(resume: MinPathResumeDto):
    edgesIdStr = ''
    if len(resume.commonEdges) == 0:
      edgesIdStr = '-1'
    else:
      commonEdges = sorted(resume.commonEdges)
      edgesIdStr = ' '.join(str(edgeId) for edgeId in commonEdges)
    print(f'Parte 3: {edgesIdStr}')
