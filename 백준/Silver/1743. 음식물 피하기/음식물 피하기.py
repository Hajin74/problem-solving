from collections import deque

N, M, K = map(int, input().split())
graph = [[0] * M for _ in range(N)]
for _ in range(K):
  y, x = map(int, input().split())
  graph[y - 1][x - 1] = 1
#print(graph)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(y, x):
  queue = deque()
  queue.append((y, x))
  graph[y][x] = 0

  size = 0
  while queue:
    # print(queue)
    y, x = queue.popleft()
    size += 1
    for i in range(4):
      ny, nx = y + dy[i], x + dx[i]
      if (0 <= ny < N) and (0 <= nx < M) and graph[ny][nx] == 1:
        queue.append((ny, nx))
        graph[ny][nx] = 0
        
  return size

  
result = []
for i in range(N):
  for j in range(M):
    if graph[i][j] == 1:
      result.append(bfs(i, j))

print(max(result))