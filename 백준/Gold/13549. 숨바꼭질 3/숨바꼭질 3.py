import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
MAX = 100001

N, K = map(int, input().split())

def dijkstra(N, K):
    shortest = [INF] * MAX
    shortest[N] = 0 # 시작점 초기화

    h_queue = []
    heapq.heappush(h_queue, (0, N))

    while h_queue:
        weight, now = heapq.heappop(h_queue)

        # nx = 이동한 X, 걸린 시간(초)
        for nx in [(now+1, 1), (now-1, 1), (2*now, 0)]:
            next = nx[0]
            time = nx[1]
            cost = weight + time

            # 범위 제한
            if 0 <= next < MAX and shortest[next] > cost:
                shortest[next] = cost
                heapq.heappush(h_queue, (cost, next))

    print(shortest[K])

dijkstra(N, K)