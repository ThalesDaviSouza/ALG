from Services.maxIsoscelesFinder import MaxIsoscelesFinder
from Services.minPerimeterFinder import MinPerimeterFinder

# h = MaxIsoscelesFinder.getAlturaMax([5, 6, 5, 8, 9, 10, 5, 8, 9, 5, 7, 9, 9, 9, 6, 3])
# h = MaxIsoscelesFinder.getAlturaMax([5, 1, 1, 1, 1, 1, 1, 3])
# h = MaxIsoscelesFinder.getAlturaMax([1, 4, 1, 4, 1, 6, 7, 1, 9])
# print(f"Parte 1: {h}")
# points = [(0, 0), (1, 1), (3, 0), (0, 3), (12, 10), (3, 3)]
# points = [(0, 0), (0, 1), (1, 0)]
points = [(15, 2),
  (0, 0), (1, 1), (3, 0), (0, 3), (12, 10), (3, 3),
  (2, 5), (7, 2), (4, 8), (9, 1), (6, 6), (1, 9),
  (8, 4), (5, 7), (10, 3), (2, 12), (11, 8), (7, 11),
  (13, 5), (4, 14), (8, 15), (16, 7), (3, 17),
  (18, 4), (9, 18), (19, 9), (5, 20), (20, 12), (10, 21),
  (1, 13), (17, 3), (6, 16), (21, 6), (11, 19),
  (22, 10), (7, 22), (23, 13), (12, 23), (24, 8), (8, 24),
  (25, 15), (13, 25), (26, 5), (14, 26), (27, 17), (15, 27),
  (28, 11), (17, 28), (29, 19), (17, 29), (30, 7), (18, 30),
  (2, 2), (4, 4), (6, 8), (8, 12), (10, 16), (12, 20),
  (14, 24), (16, 28), (18, 2), (20, 6), (22, 10), (24, 14),
  (26, 18), (28, 22), (30, 26), (1, 6), (3, 10), (5, 14),
  (7, 18), (9, 22), (11, 26), (13, 30), (15, 4), (17, 8),
  (19, 12), (21, 16), (23, 20), (25, 24), (27, 28), (29, 2),
  (2, 8), (4, 12), (6, 16), (8, 20), (10, 24), (12, 28),
  (14, 2), (16, 6), (18, 10), (20, 14), (22, 18), (24, 22),
  (26, 26), (28, 30), (30, 4), (1, 11), (3, 15), (5, 19),
  (7, 23), (9, 27), (11, 1), (13, 5), (15, 9), (17, 13),
  (19, 17), (21, 21), (23, 25), (25, 29), (27, 3), (29, 7), (14, 1)
]
perimetroMin, trianguloEncontrado = MinPerimeterFinder.getMinPerimeter(points)
idsTriangulo = sorted([p.id for p in trianguloEncontrado])
stringIdsTriangulo = ""
for id in idsTriangulo:
  stringIdsTriangulo += f"{id} "

print(f"Parte 2: {perimetroMin:.4f} {stringIdsTriangulo}")