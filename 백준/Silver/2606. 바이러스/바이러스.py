# from collections import deque
import sys

n = int(input())  # 컴퓨터 수
m = int(input())  # 네트워크 수
graph = [[] for _ in range(n+1)] # 인접 리스트

# 네트워크 입력받기
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)

visited = [False] * (n+1)

def dfs(graph, v, visited):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


dfs(graph, 1, visited)

# 본 컴퓨터 빼고 바이러스에 걸리게 되는 컴퓨터 수 출력   
print(visited.count(True) - 1)