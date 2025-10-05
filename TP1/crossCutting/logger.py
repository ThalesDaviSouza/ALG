from domain.graph import Graph
from infra.graphFind import FindResume

class Logger:
  def logGraph(graph: Graph):
    print('Grafo:')
    for id in sorted(graph.graph.keys()):
      edgesIds = graph.graph[id].keys()
      edges_str = ', '.join(str(graph.graph[id][edgeId]) for edgeId in edgesIds)
      print(f'{id} -> [{edges_str}]')
  
  def logFindResume(resume: FindResume):
    print(f'{resume.distances}: distances')
    print(f'{resume.predecessor}: predecessor')
    print(f'{resume.shortestPathsEdges}: shortestPathsEdges')