from collections import deque

N, M = map(int, input().split())

graph = []
for _ in range(N):
     graph.append(list(map(int, input())))
# print(graph)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 방문하지 않은거 큐에 넣고 방문처리

def bfs(n, m):
    queue = deque()
    queue.append((n, m))

    graph[n][m] = 1 # 현재 방문 처리

    # 큐가 빌 때까지
    while queue:
        x, y = queue.popleft()

        # 주변 탐색
        for i in range(4):
            nx, ny = x + dx[i], y+ dy[i]

            # 범위 제한하기
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
bfs(0, 0)
print(graph[N-1][M-1])

