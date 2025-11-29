from combiner import combine_sides, get_conflicts_right
from right_part import get_sizes_right
from graph import create_adjacency_masks, split_graph

inputs = input().split(' ')

qtdDuentes = int(inputs[0])
qtdConflicts = int(inputs[1])
edges = []

for i in range(0, qtdConflicts):
  inputs = input().split(' ')
  u = int(inputs[0]) 
  v = int(inputs[1])
  pair = (u,v)
  edges.append(pair) 


adj = create_adjacency_masks(qtdDuentes, edges)

nLeft, nRight, adjLeft, adjRight, mapLeft, mapRight = split_graph(qtdDuentes, adj)

sizes, masks = get_sizes_right(nRight, adjRight)

conflictR = get_conflicts_right(nLeft, adj, mapLeft, mapRight)

best_size, best_vertices = combine_sides(
  nLeft, nRight, adjLeft, sizes, masks, conflictR, mapLeft, mapRight
)

print(best_size)
print(*best_vertices)
