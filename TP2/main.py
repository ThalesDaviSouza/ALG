from Services.maxIsoscelesFinder import MaxIsoscelesFinder
from Services.minPerimeterFinder import MinPerimeterFinder

numPilhas = int(input())
pilhasStr = input()
pilhas = list(map(int, pilhasStr.split()))

h = MaxIsoscelesFinder.getAlturaMax(pilhas)

print(f"Parte 1: {h}")


numPoints = int(input())
points = []
for i in range(numPoints):
  linha = input()
  coordenadas = list(map(int, linha.split()))
  points.append((coordenadas[0], coordenadas[1]))

perimetroMin, trianguloEncontrado = MinPerimeterFinder.getMinPerimeter(points)

idsTriangulo = sorted([p.id for p in trianguloEncontrado])
stringIdsTriangulo = ""
for id in idsTriangulo:
  stringIdsTriangulo += f"{id} "

print(f"Parte 2: {perimetroMin:.4f} {stringIdsTriangulo}")