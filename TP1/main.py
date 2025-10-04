from application.graphOrquestration import GraphOrquestration
from crossCutting.logger import Logger
from domain.graph import Graph

graph = Graph()

GraphOrquestration.analyzeCity(graph, "teste.txt")

Logger.logGraph(graph)
