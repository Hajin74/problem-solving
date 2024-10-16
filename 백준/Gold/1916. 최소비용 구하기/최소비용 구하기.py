import heapq
import sys

INF = 1e9
input = sys.stdin.readline

N = int(input()) # 도시 개수
M = int(input()) # 버스 개수

graph = [[] for _ in range(N+1)] # 버스 비용 정보
shortest_path = [INF] * (N+1) # 최단 경로 초기화

for _ in range(M):
    a, b, c = map(int, input().split()) # a에서 b로 드는 비용 c
    graph[a].append((b, c))

departure, arrival = map(int, input().split()) # 출발 도시, 도착 도시

def dijkstra(start):
    queue = []

    # 출발 도시 초기화
    heapq.heappush(queue, (0, start))
    shortest_path[start] = 0

    while queue:
        # 최단 경로 큐 꺼내기
        distance, now = heapq.heappop(queue)
        
        if distance > shortest_path[now]:
            continue

        # 인접 노드 탐색
        for tuple in graph[now]:
            next = tuple[0]
            weight = tuple[1]

            cost = distance + weight # 현재 큐의 최단 경로를 거쳐서 + 다음 노드로 가는 가중치

            if cost < shortest_path[next]:
                shortest_path[next] = cost
                heapq.heappush(queue, (cost, next))

dijkstra(departure)

print(shortest_path[arrival])