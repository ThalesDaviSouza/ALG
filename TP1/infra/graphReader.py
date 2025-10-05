import sys
from domain.graph import Graph

# Classe responsável por armazenar a lógica de leitura dos grafos
class GraphReader:
  # Função para ler o grafo da entrada 
  def readInput(graph: Graph) -> bool:
    lines = []
    
    if len(sys.argv) > 1: # Tenta ler da linha de comando
      with open(sys.argv[1], "r") as file:
        lines = file.readlines()  
    elif not sys.stdin.isatty(): # Tenta ler do stdin
      lines = sys.stdin.readlines()
    else: # Se falhar retorna erro
      return False

    # Lê os dados no topo do arquivo
    firstLine = lines[0].strip().split()
    numVertices, numEdges = map(int, firstLine)
    
    graph.numVertices = numVertices
    graph.numEdges = numEdges
    
    # Ler as demais linhas
    for id, line in enumerate(lines[1:]):
      line = line.strip()
      if not line:
          continue
      origin, dest, weight = map(int, line.split())
      GraphReader.readEdge(graph, id+1, origin, dest, weight)
    
    # Retorna True se não tiver erro durante a leitura
    return True

  # Lógica de leitura dos vértices para otimizar o Dijkstra futuramente
  def readEdge(graph: Graph, id: int, origin: int, dest: int, weight: int):
    # Ciclos não são úteis para o problema em questão
    if origin == dest:
      return

    actualEdge = graph.getEdge(origin, dest)

    # Caso não tenha nenhuma aresta adicionada entre os dois vértices
    # Adiciona a aresta
    if actualEdge is None:
      graph.addEdge(id, origin, dest, weight)
      return
    
    # Caso a aresta atual tenha um custo maior do que a aresta sendo lida
    # Troca a aresta
    if actualEdge.weight > weight:
      graph.addEdge(origin, dest, weight)
      

