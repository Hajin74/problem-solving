from collections import deque

N, K = map(int, input().split())
max_loc = 100000
visited = [0] * (max_loc + 1)

def bfs(start):
  queue = deque([start])
  while queue:
    x = queue.popleft()
    
    if x == K:
      print(visited[x])
      break

    for i in (x-1, x+1, x*2):
      if 0 <= i <= max_loc and not visited[i]:
        visited[i] = visited[x] + 1
        queue.append(i)
    

bfs(N)