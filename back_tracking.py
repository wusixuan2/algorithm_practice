graph1 = {
          0: [1, 2, 3],
          1: [4],
          2: [4, 5],
          3: [4,5],
          4: [],
          5: [6],
          6:[]
          }
# finds route from orig to dest in G if it exists
def find_route(graph, orig, dest, visited):
  if orig == dest: return [orig]

  outdegree = graph[orig]
  visited.append(orig)
  route = find_route_list(graph, outdegree, dest, visited)

  if not route: return False

  route.insert(0, orig)
  return route

# produces route from an element of los to dest in G, if one exists
def find_route_list(graph, outdegree, dest, visited):
  if not outdegree: return False
  if outdegree[0] not in visited:
    route = find_route(graph, outdegree[0], dest, visited) # try the first node
    if route: return route
  return find_route_list(graph, outdegree[1:], dest, visited) # not in the first node, try looking at the rest

# print(find_route(graph1, 0, 6, []))

# abs(Q1 row - Q2 row) == abs(Q1 col - Q2 col) => same diagonal
# partial_sol = []
# for c in board:
#   partial_sol.append('.' * c + 'Q' + '.' * (n - c - 1))
# res.append(partial_sol)
def solveNQueens(n, row=0, board=None, res=[]):
  if not board: board, res = [0] * n, []
  if row == n:
    res.append(['.' * c + 'Q' + '.' * (n - c - 1) for c in board])
    return
  for col in range(n):
    if col not in board[:row] and all(row - r != abs(col - board[r]) for r in range(row)):
      board[row] = col
      solveNQueens(n, row + 1, board, res)
  return res




print(solveNQueens(4))



