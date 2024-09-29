from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        curr_node = queue.popleft()
        for next_node in graph[curr_node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)

visited = [False for _ in range(n+1)]
count = 0
for i in range(1, n+1):
    if not visited[i]:
        bfs(graph, i, visited)
        count += 1

print(count)