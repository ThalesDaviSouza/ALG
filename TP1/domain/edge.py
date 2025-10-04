class Edge:
  def __init__(self, dest: int, weight: int):
    self.weight = weight
    self.destination = dest
  
  def __str__(self):
    return f'({self.destination}, {self.weight})'