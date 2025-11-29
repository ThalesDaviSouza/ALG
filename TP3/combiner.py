def get_conflicts_right(nLeft, adj, mapLeft, mapRight):
  conflictsRight = [0] * nLeft

  for iLeft, verticeLeft in enumerate(mapLeft):
    mask = 0
    for jRight, verticeRight in enumerate(mapRight):
      # Verifica se há conflito entre vértice da esquerda e vértice da direita
      if (adj[verticeLeft] >> verticeRight) & 1:
        # Seta bit na posição j para indicar conflito
        mask |= (1 << jRight)
    conflictsRight[iLeft] = mask

  return conflictsRight


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

  # Máscara com todos os vértices da direita (todos bits = 1)
  allRightsEdges = (1 << nRight) - 1

  # Itera por todos os subconjuntos da parte esquerda
  for S in range(1 << nLeft):
    # Verifica se S é conjunto independente
    independent = True
    for v in range(nLeft):
      if (S >> v) & 1:
        # Verifica se vértice v tem conflito com outros vértices em S
        if S & adjLeft[v]:
          independent = False
          break
    if not independent:
      continue

    # Calcula vértices que tem conflitos na direita (conflitam com escolhas da esquerda)
    conflicts = 0
    for v in range(nLeft):
      if (S >> v) & 1:
        # Adiciona todos os conflitos do vértice v da esquerda
        conflicts |= conflictR[v]

    # Vértices permitidos na direita = todos que não tem conflitos com vertices da esquerda
    allowed = allRightsEdges & ~conflicts

    # Tamanho total = vértices da esquerda + melhor solução da direita permitida
    size_total = bin(S).count("1") + sizes[allowed]

    # Constrói a solução completa
    solution = []

    # Adiciona vértices da esquerda selecionados
    for v in range(nLeft):
      if (S >> v) & 1:
        solution.append(mapLeft[v])

    # Adiciona vértices da direita da solução ótima
    maskRight = masks[allowed]
    for j in range(nRight):
      if (maskRight >> j) & 1:
        solution.append(mapRight[j])

    solution.sort()

    # Atualiza melhor solução encontrada
    if size_total > best_size:
      best_size = size_total
      best_vertices = solution
    elif size_total == best_size:
      # Desempate: escolhe a solução lexicograficamente menor
      if solution < best_vertices:  
        best_vertices = solution

  return best_size, best_vertices