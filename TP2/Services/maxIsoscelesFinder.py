class MaxIsoscelesFinder:
  
  def getAlturaMax(pilhas):
    numPilhas = len(pilhas)
    alturasMaxsTeoricas = [-1 for _ in range(numPilhas)]
    
    for i in range(int(numPilhas/2)+1):
      j = numPilhas-i-1
      alturaMaxPosicao = i+1

      alturaMaxPos = MaxIsoscelesFinder.getAlturaMaxPos(pilhas, i, alturaMaxPosicao, alturasMaxsTeoricas)
      alturasMaxsTeoricas[i] = alturaMaxPos
      
      if j != i:
        alturaMaxPos = MaxIsoscelesFinder.getAlturaMaxPos(pilhas, j, alturaMaxPosicao, alturasMaxsTeoricas)
        alturasMaxsTeoricas[j] = alturaMaxPos

    print(alturasMaxsTeoricas)
    return max(alturasMaxsTeoricas)

  def getAlturaMaxPos(pilhas, index, alturaMaxPosicao, alturasMaxsTeoricas):
    if index == 0 or index == (len(pilhas)-1):
      return 1
    
    alturaMaxIsolada = min(alturaMaxPosicao, pilhas[index])

    alturaMaxPos = alturaMaxIsolada
    
    # esquerda
    if alturasMaxsTeoricas[index-1] != -1:
      alturaMaxPos = min(alturaMaxPos, alturasMaxsTeoricas[index-1]+1) 
    else:
      alturaMaxPos = min(alturaMaxPos, pilhas[index-1]+1)
    
    # direita
    if alturasMaxsTeoricas[index+1] != -1:
      alturaMaxPos = min(alturaMaxPos, alturasMaxsTeoricas[index+1]+1) 
    else:
      alturaMaxPos = min(alturaMaxPos, pilhas[index+1]+1)
    

    return alturaMaxPos

