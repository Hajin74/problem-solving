import sys

sys.setrecursionlimit(10**7)


def dfs(n, m):
  if n < 0 or n >= N or m < 0 or m >= M:
    return False

  if graph[n][m] == 1:
    graph[n][m] = 0
    dfs(n - 1, m)
    dfs(n + 1, m)
    dfs(n, m - 1)
    dfs(n, m + 1)
    return True

  return False


T = int(input())

result = [0] * T
for t in range(T):
  M, N, Y = map(int, input().split())

  graph = [[0 for _ in range(M)] for _ in range(N)]
  for _ in range(Y):
    m, n = map(int, input().split())
    graph[n][m] = 1

  result[t] = 0
  for n in range(N):
    for m in range(M):
      if dfs(n, m):
        result[t] += 1

for r in result:
  print(r)
