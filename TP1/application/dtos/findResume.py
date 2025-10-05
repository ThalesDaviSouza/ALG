class FindResumeDto:
  def __init__(self, distances, predecessor: list[list], shortestPathsEdges):
    self.distances = distances
    self.predecessor = predecessor
    self.shortestPathsEdges = shortestPathsEdges
