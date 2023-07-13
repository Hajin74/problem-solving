import sys

sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
  u, v = map(int, sys.stdin.readline().split())
  graph[u].append(v)
  graph[v].append(u)


def dfs(graph, v, visited):
  if visited[v]:
    return False

  visited[v] = True
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)
  return True


result = 0
visited = [False] * (N + 1)
for i in range(1, N + 1):
  if dfs(graph, i, visited):
    result += 1

print(result)
