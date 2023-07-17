import sys

sys.setrecursionlimit(10**6)


def dfs(w, h):
  if w < 0 or w >= W or h < 0 or h >= H:
    return False

  if graph[h][w] == 1:
    graph[h][w] = 0
    dfs(w - 1, h - 1)
    dfs(w, h - 1)
    dfs(w + 1, h - 1)
    dfs(w - 1, h)
    dfs(w + 1, h)
    dfs(w - 1, h + 1)
    dfs(w, h + 1)
    dfs(w + 1, h + 1)
    return True

  return False


W, H = map(int, input().split())
result = []
while W != 0 and H != 0:
  graph = []
  for _ in range(H):
    data = list(map(int, input().split()))
    graph.append(data)

  count = 0
  for h in range(H):
    for w in range(W):
      if dfs(w, h):
        count += 1
  result.append(count)

  W, H = map(int, input().split())

for r in result:
  print(r)
