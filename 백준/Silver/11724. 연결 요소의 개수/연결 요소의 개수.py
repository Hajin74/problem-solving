import sys
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(graph, v, visited):
    visited[v] = True

    for next_node in graph[v]:
        if not visited[next_node]:
            dfs(graph, next_node, visited)
    
visited = [False for _ in range(n+1)]
count = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(graph, i, visited)
        count += 1

print(count)