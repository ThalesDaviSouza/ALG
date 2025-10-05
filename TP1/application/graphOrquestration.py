from crossCutting.logger import Logger
from domain.graph import Graph
from infra.graphFind import GraphFind
from infra.graphReader import GraphReader


class GraphOrquestration:
  def analyzeCity(graph: Graph, path: str):
    GraphReader.readInput(graph, path)

    resume = GraphFind.Dijkstra(graph, 1)
    minPathResume = GraphFind.getMinPathEdgesId(resume, 1, graph.numVertices)

    Logger.logMinPathLength(resume, graph.numVertices)
    Logger.logMinPathEdgesId(minPathResume)
    Logger.logCriticalEdges(minPathResume)
