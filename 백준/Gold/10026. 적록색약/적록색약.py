import copy
import sys

sys.setrecursionlimit(10**7)

N = int(input())

graph = []
for _ in range(N):
  graph.append(list(map(str, input())))
graph2 = copy.deepcopy(graph)


def dfs(x, y, color, graph):
  if x < 0 or x >= N or y < 0 or y >= N:
    return False

  if graph[x][y] != "V" and graph[x][y] == color:
    graph[x][y] = "V"

    dfs(x + 1, y, color, graph)
    dfs(x - 1, y, color, graph)
    dfs(x, y + 1, color, graph)
    dfs(x, y - 1, color, graph)

    return True

  return False


result1 = 0
for i in range(N):
  for j in range(N):
    if dfs(i, j, graph[i][j], graph):
      result1 += 1

for i in range(N):
  for j in range(N):
    if graph2[i][j] == "G":
      graph2[i][j] = "R"

result2 = 0
for i in range(N):
  for j in range(N):
    if dfs(i, j, graph2[i][j], graph2):
      result2 += 1

print(result1, result2)
