import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
start = int(input())

graph = [[] for _ in range(V+1)] # 노드 개수만큼 인접 노드를 표현할 수 있는 2차원 배열
distances = [INF] * (V+1)

for _ in range(E):
    u, v, w = map(int, input().split()) # u에서 v로 가는 가중치 w
    graph[u].append((v, w)) 

def dijkstra(start):
    queue = [] # 우선순위 큐

    # 출발지 노드 큐에 삽입
    heapq.heappush(queue, (0, start))
    distances[start] = 0 # 최단 경로 0으로 초기화

    while queue:
        # 가장 거리가 짧은 최단 경로 가져오기
        distance, now = heapq.heappop(queue) # O(logV)로 가져올 수 있음

        # 이미 최단 경로가 정해진 경우 == 방문 했던 노드
        if distances[now] < distance:
            continue

        # 인접한 노드 탐색
        # graph[노드 번호] = (인접 노드 번호, 가중치)
        for tuple in graph[now]:
            next = tuple[0]
            weight = tuple[1]
            
            cost = distance + weight

            # 인접 노드로 갈 때, 현재 노드를 거쳐 가는 것이 더 짧으면 갱신
            if cost < distances[next]: # 거쳐 가는 비용 < 현재 최단 거리 테이블
                distances[next] = cost
                heapq.heappush(queue, (cost, next)) # 우선순위 큐에 넣기

dijkstra(start)

# 출력
for i in range(1, V+1):
    if distances[i] == INF: # 갈 수 없는 경우
        print("INF")
    else:
        print(distances[i])