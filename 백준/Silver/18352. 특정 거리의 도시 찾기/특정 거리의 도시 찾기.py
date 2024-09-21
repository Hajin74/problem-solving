from collections import deque
import sys

n, m, k, x = map(int, input().split()) # 도시, 도로, 최단거리, 출발도시
graph = [[] for _ in range(n+1)] # 도시만큼 인접 리스트 만들기

# 해당하는 도시에 도로 추가하기
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

# 거리 기록하기
distance = [-1] * (n+1)
distance[x] = 0 # 출발지는 거리 0으로 초기화

queue = deque([x])
while queue:
    now = queue.popleft() 

    # 현재 노드에서 인접한 노드 방문해서
    for i in graph[now]:
        if distance[i] == -1: # 처음 방문한 노드이면
            distance[i] = distance[now] + 1 # 최단 거리 기록
            queue.append(i)

check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)
