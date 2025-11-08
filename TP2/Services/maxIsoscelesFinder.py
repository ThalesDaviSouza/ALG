UNDEFINED = -1

class MaxIsoscelesFinder:

  def getAlturaMax(pilhas):
    numPilhas = len(pilhas)

    esquerda = [0] * numPilhas
    direita = [0] * numPilhas

    # encontro a altura máxima andando pela esquerda
    esquerda[0] = 1
    for i in range(1, numPilhas):
      esquerda[i] = min(pilhas[i], esquerda[i-1] + 1)

    # encontro a altura máxima andando pela direita
    direita[numPilhas-1] = 1
    for i in range(numPilhas-2, -1, -1):
      direita[i] = min(pilhas[i], direita[i+1] + 1)

    # encontro a altura máxima para o ponto
    alturas = [min(esquerda[i], direita[i]) for i in range(numPilhas)]

    return max(alturas)

