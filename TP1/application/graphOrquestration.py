from domain.graph import Graph
from infra.graphFind import GraphFind, Resumo
from infra.graphReader import GraphReader


class GraphOrquestration:
  def analyzeCity(graph: Graph, path: str):
    GraphReader.readInput(graph, path)

    resume = GraphFind.Dijkstra(graph, 1)

    print(resume.distances)
    print(resume.predecessor)