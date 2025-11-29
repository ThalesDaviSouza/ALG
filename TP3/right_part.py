def get_sizes_right(nRight, adjRight):
  # Total de subconjuntos possíveis (2^nRight)
  n = 1 << nRight  

  # Tamanho do maior conjunto independente para cada bitmask
  sizes = [0] * n 
  # Máscara representando o conjunto independente ótimo
  masks = [0] * n   

  # Itera por todos os subconjuntos não vazios
  for bitmask in range(1, n):
    # Pega o bit menos significativo (último vértice adicionado)
    lowestbit = bitmask & -bitmask
    # Converte a posição do bit para índice do vértice
    verticeId = (lowestbit.bit_length() - 1)

    # Remove o vértice atual do conjunto
    bitmaskReduced = bitmask & ~(1 << verticeId)

    # Calcula vértices permitidos: remove os adjacentes ao vértice atual
    # ~adjRight[verticeId] inverte os bits - 0 onde há conflito, 1 onde não há
    adjacentes = bitmaskReduced & ~adjRight[verticeId]

    # Duas opções: não incluir o vértice ou incluí-lo
    option1 = sizes[bitmaskReduced] # Não incluir o vértice
    option2 = 1 + sizes[adjacentes] # Incluir o vértice (remove adjacentes)

    # Máscaras correspondentes a cada opção
    mask1 = masks[bitmaskReduced]
    mask2 = (1 << verticeId) | masks[adjacentes]

    # Escolhe a melhor opção
    if option2 > option1:
      sizes[bitmask] = option2
      masks[bitmask] = (1 << verticeId) | masks[adjacentes]

    elif option1 == option2:
       # Desempate: escolhe a máscara lexicograficamente menor
      if mask2 < mask1:
        masks[bitmask] = mask2
      else:
        masks[bitmask] = mask1
      sizes[bitmask] = option1
      
    else:
      sizes[bitmask] = option1
      masks[bitmask] = masks[bitmaskReduced]

  return sizes, masks