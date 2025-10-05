from application.dtos.findResume import FindResumeDto
from application.dtos.minPathResume import MinPathResumeDto
from domain.graph import Graph
from infra.graphFind import GraphFind

class Logger:
  def logGraph(graph: Graph):
    print('Grafo:')
    for id in sorted(graph.graph.keys()):
      edgesIds = graph.graph[id].keys()
      edges_str = ', '.join(str(graph.graph[id][edgeId]) for edgeId in edgesIds)
      print(f'{id} -> [{edges_str}]')
  
  def logFindResume(resume: FindResumeDto):
    print(f'{resume.distances}: distances')
    print(f'{resume.predecessor}: predecessor')
    print(f'{resume.shortestPathsEdges}: shortestPathsEdges')

  def logMinPathLength(resume: FindResumeDto, dest: int):
    destId = GraphFind.getArrayId(dest)
    print(f'Parte 1: {resume.distances[destId]}')
  
  def logMinPathEdgesId(resume: MinPathResumeDto):
    edgesIdStr = ' '.join(str(edgeId) for edgeId in resume.minPathsEdges)
    print(f'Parte 2: {edgesIdStr}')
  
  def logCriticalEdges(resume: MinPathResumeDto):
    edgesIdStr = ''
    if len(resume.minPaths) == 0:
      edgesIdStr = '-1'
    else:
      edgesIdStr = ' '.join(str(edgeId) for edgeId in resume.minPaths)
    print(f'Parte 3: {edgesIdStr}')
