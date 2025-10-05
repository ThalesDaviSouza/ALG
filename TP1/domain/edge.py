class Edge:
  def __init__(self, id: int, dest: int, weight: int):
    self.id = id
    self.weight = weight
    self.destination = dest
  
  def __str__(self):
    return f'({self.destination}, {self.weight})'