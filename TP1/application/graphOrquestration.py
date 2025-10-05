from crossCutting.logger import Logger
from domain.graph import Graph
from infra.graphFind import GraphFind
from infra.graphReader import GraphReader


class GraphOrquestration:
  # Função feita para organizar as chamadas de função para analisar a cidade
  def analyzeCity(graph: Graph):
    # Ler os dados do grafo
    success = GraphReader.readInput(graph)
    if not success:
      print('Houve um erro na leitura do arquivo')
      return

    # Realizar busca dos menores caminhos
    resume = GraphFind.Dijkstra(graph, 1)

    # Obter as respostas para as partes 2 e 3
    minPathResume = GraphFind.getMinPathEdgesId(resume, 1, graph.numVertices)

    # Imprimir a resposta da parte 1
    Logger.logMinPathLength(resume, graph.numVertices)
    # Imprimir a resposta da parte 2
    Logger.logMinPathEdgesId(minPathResume)
    # Imprimir a resposta da parte 3
    Logger.logCriticalEdges(minPathResume)
