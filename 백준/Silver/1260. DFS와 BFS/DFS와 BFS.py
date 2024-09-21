import sys
from collections import deque

n, m, v = map(int, input().split()) # 정점 개수, 간선 개수, 시작 정점
graph = [[] for _ in range(n+1)]

# 간선 입력받기 (양방향)
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 정점 작은 것부터 정렬
for i in range(1, n+1):
    graph[i].sort()
# print(graph)

# dfs로 방문하기
visited = [False] * (n+1)
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, v, visited)
print()

# bfs로 방문하기
visited = [False] * (n+1)
def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        now = queue.popleft()
        print(now, end=' ')

        for i in graph[now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(graph, v, visited)