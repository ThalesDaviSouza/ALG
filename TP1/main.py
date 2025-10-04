from crossCutting.logger import Logger
from domain.graph import Graph
from infra.graphReader import GraphReader

graph = Graph()

GraphReader.readInput(graph, "teste.txt")



# GraphReader.readEdge(graph, 2, 1, 10)
# GraphReader.readEdge(graph, 3, 2, 20)
# GraphReader.readEdge(graph, 4, 5, 30)
# GraphReader.readEdge(graph, 1, 2, 40)
# GraphReader.readEdge(graph, 5, 3, 50)
# GraphReader.readEdge(graph, 5, 3, 500)
# GraphReader.readEdge(graph, 5, 3, 20)

Logger.logGraph(graph)
