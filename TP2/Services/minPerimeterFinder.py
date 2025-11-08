class Point:
  def __init__(self, x: float, y: float, id_: int):
    if not isinstance(x, (int, float)):
      raise TypeError("x deve ser numérico.")
    if not isinstance(y, (int, float)):
      raise TypeError("y deve ser numérico.")
    if not isinstance(id_, int):
      raise TypeError("id deve ser um inteiro.")

    self.x = x
    self.y = y
    self.id = id_

  def __repr__(self):
    return f"Point(id={self.id}, x={self.x}, y={self.y})"


def distancia(p1: Point, p2: Point):
  return  ((p1.x - p2.x)**2 + (p1.y - p2.y)**2) ** 0.5


def perimetro(a: Point, b: Point, c: Point):
  return distancia(a, b) + distancia(b, c) + distancia(c, a)


def strip_closest_triangle(subconjunto, menorPerimetro):
  tam = len(subconjunto)
  melhorTri = None

  for i in range(tam):
    for j in range(i+1, min(i+21, tam)):
      for k in range(j+1, min(i+21, tam)):
        p = perimetro(subconjunto[i], subconjunto[j], subconjunto[k])

        if p < menorPerimetro:
          menorPerimetro = p
          melhorTri = (subconjunto[i], subconjunto[j], subconjunto[k])

  return menorPerimetro, melhorTri


def closest_triangle_rec(px, py):
  numPoints = len(px)

  if numPoints < 3:
    return float("inf"), None

  if numPoints == 3:
    p = perimetro(px[0], px[1], px[2])
    return p, (px[0], px[1], px[2])

  metade = numPoints // 2
  metadeX = px[metade].x

  esquerdaX = px[:metade]
  direitaX = px[metade:]

  esquerdaY = []
  direitaY = []

  for p in py:
    if p.x < metadeX:
      esquerdaY.append(p)
    else:
      direitaY.append(p)

  perE, triE = closest_triangle_rec(esquerdaX, esquerdaY)
  perD, triD = closest_triangle_rec(direitaX, direitaY)

  if perE < perD:
    menorPerimetro = perE
    melhorTri = triE
  else:
    menorPerimetro = perD
    melhorTri = triD

  subconjunto = [p for p in py if abs(p.x - metadeX) < menorPerimetro / 2]

  perS, triS = strip_closest_triangle(subconjunto, menorPerimetro)

  if perS < menorPerimetro:
    return perS, triS

  return menorPerimetro, melhorTri


class MinPerimeterFinder:

  def getMinPerimeter(points):
    pointsFormated = []
    id = 1
    for p in points:  
      pointsFormated.append(Point(p[0], p[1], id))
      id += 1

    px = sorted(pointsFormated, key=lambda p: p.x)
    py = sorted(pointsFormated, key=lambda p: p.y)

    return closest_triangle_rec(px, py)
