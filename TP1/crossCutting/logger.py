from domain.graph import Graph

class Logger:
  def logGraph(graph: Graph):
    print('Grafo:')
    for id in sorted(graph.graph.keys()):
      edgesIds = graph.graph[id].keys()
      edges_str = ', '.join(str(graph.graph[id][edgeId]) for edgeId in edgesIds)
      print(f'{id} -> [{edges_str}]')