computer = int(input())
connected_pair = int(input())

graph = [[] for _ in range(computer + 1)]
for i in range(connected_pair):
  n, m = map(int, input().split())
  graph[n].append(m)
  graph[m].append(n)

def dfs(graph, v, visited):
  visited[v] = True
  for i in graph[v]:
    if visited[i] == False:
      dfs(graph, i, visited)


visited = [False] * (computer + 1)
dfs(graph, 1, visited)

print(visited.count(True) - 1)