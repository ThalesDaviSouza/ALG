def create_adjacency_masks(qtd, edges):
  adj = [0] * qtd
  for duente1, duente2 in edges:
    adj[duente1] |= (1 << duente2)
    adj[duente2] |= (1 << duente1)
  return adj

def split_graph(n, adj):
  nLeft = n // 2
  nRight = n - nLeft

  mapLeft = list(range(nLeft))
  mapRight = list(range(nLeft, n))

  adjLeft = [0] * nLeft
  adjRight = [0] * nRight

  for i in range(nLeft):
    for j in range(nLeft):
      if (adj[i] >> j) & 1:
        adjLeft[i] |= (1 << j)

  for i, v in enumerate(mapRight):
    for j, u in enumerate(mapRight):
      if (adj[v] >> u) & 1:
        adjRight[i] |= (1 << j)

  return nLeft, nRight, adjLeft, adjRight, mapLeft, mapRight
