def get_sizes_right(nRigth, adjRight):
  n = 1 << nRigth
  sizes = [0] * n
  masks = [0] * n

  for bitmask in range(1, n):
    lowestbit = bitmask & -bitmask
    verticeId = (lowestbit.bit_length() - 1)

    # Bitmask sem o vertice em questão
    bitmaskReduced = bitmask & ~(1 << verticeId)

    # Adjacentes (duentes com "briga") da Bitmask sem o vertice
    adjacentes = bitmaskReduced & ~adjRight[verticeId]

    option1 = sizes[bitmaskReduced]
    option2 = 1 + sizes[adjacentes]

    mask1 = masks[bitmaskReduced]
    mask2 = (1 << verticeId) | masks[adjacentes]

    if option2 > option1:
      sizes[bitmask] = option2
      masks[bitmask] = (1 << verticeId) | masks[adjacentes]
    elif option1 == option2:
       # comparação lexicográfica
      if mask2 < mask1:
        masks[bitmask] = mask2
      else:
        masks[bitmask] = mask1
      sizes[bitmask] = option1
      
    else:
      sizes[bitmask] = option1
      masks[bitmask] = masks[bitmaskReduced]

  return sizes, masks
