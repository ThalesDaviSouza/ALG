def get_conflicts_right(nLeft, adj, mapLeft, mapRight):
  conflictsRigth = [0] * nLeft

  for iL, vL in enumerate(mapLeft):
    mask = 0
    for jR, vR in enumerate(mapRight):
      if (adj[vL] >> vR) & 1:
        mask |= (1 << jR)
    conflictsRigth[iL] = mask

  return conflictsRigth


def combine_sides(
  nLeft, 
  nRight, 
  adjLeft, 
  sizes, 
  masks, 
  conflictR, 
  mapLeft, 
  mapRight
):
  best_size = 0
  best_vertices = []

  allRightsEdges = (1 << nRight) - 1

  for S in range(1 << nLeft):
    # verifica se S é independente
    independent = True
    for v in range(nLeft):
      if (S >> v) & 1:
        if S & adjLeft[v]:
          independent = False
          break
    if not independent:
      continue

    # calcula proibidos
    forbidden = 0
    for v in range(nLeft):
      if (S >> v) & 1:
        forbidden |= conflictR[v]

    allowed = allRightsEdges & ~forbidden

    # combina com R
    size_total = bin(S).count("1") + sizes[allowed]

    # monta solução
    solution = []

    # esquerda
    for v in range(nLeft):
      if (S >> v) & 1:
        solution.append(mapLeft[v])

    # direita
    maskR = masks[allowed]
    for j in range(nRight):
      if (maskR >> j) & 1:
        solution.append(mapRight[j])

    solution.sort()

    if size_total > best_size:
      best_size = size_total
      best_vertices = solution
    elif size_total == best_size:
      if solution < best_vertices:  
        best_vertices = solution

  return best_size, best_vertices
