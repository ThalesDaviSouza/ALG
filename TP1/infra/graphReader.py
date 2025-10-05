from domain.graph import Graph

class GraphReader:
  def readInput(graph: Graph, path: str):
    with open(path, "r") as file:
      firstLine = file.readline().strip().split()
      numVertices, numEdges = map(int, firstLine)
      
      graph.numVertices = numVertices
      graph.numEdges = numEdges
      
      for id, line in enumerate(file):
        origin, dest, weight = map(int, line.strip().split())
        GraphReader.readEdge(graph, id+1, origin, dest, weight)

  def readEdge(graph: Graph, id: int, origin: int, dest: int, weight: int):
    # Ciclos não são úteis para o problema em questão
    if origin == dest:
      return;

    actualEdge = graph.getEdge(origin, dest)

    # Caso não tenha nenhuma aresta adicionada
    # Adiciona ela aresta
    if actualEdge is None:
      graph.addEdge(id, origin, dest, weight)
      return
    
    # Caso a aresta atual tenha um custo maior do que a atual
    # Troca a aresta
    if actualEdge.weight > weight:
      graph.addEdge(origin, dest, weight)
      

