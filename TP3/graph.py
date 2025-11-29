def create_adjacency_masks(qtd, edges):
  adj = [0] * qtd
  for duente1, duente2 in edges:
    # Os subconjuntos serão repesentados por máscaras binárias
      
    # Seta o bit na posição do duente 2 para indicar adjacência
    adj[duente1] |= (1 << duente2)
    
    # Seta o bit na posição do duente 1 para indicar adjacência  
    adj[duente2] |= (1 << duente1)

  return adj

def split_graph(n, adj):
  nLeft = n // 2
  nRight = n - nLeft

  # Mapeia índices originais para as novas posições nas partes
  mapLeft = list(range(nLeft))
  mapRight = list(range(nLeft, n))

  # Matrizes de adjacência para cada parte
  adjLeft = [0] * nLeft
  adjRight = [0] * nRight

  # Constrói adjacências da parte esquerda
  for i in range(nLeft):
    for j in range(nLeft):
      # Verifica se há aresta entre i e j no grafo original
      if (adj[i] >> j) & 1:
        # Seta bit na posição j para indicar adjacência
        adjLeft[i] |= (1 << j)

  # Constrói adjacências da parte direita
  for i, v in enumerate(mapRight):
    for j, u in enumerate(mapRight):
      # Verifica se há aresta entre v e u no grafo original
      if (adj[v] >> u) & 1:
        # Seta bit na posição j para indicar adjacência
        adjRight[i] |= (1 << j)

  return nLeft, nRight, adjLeft, adjRight, mapLeft, mapRight