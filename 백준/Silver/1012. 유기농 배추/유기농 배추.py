# 이것도 최단경로를 구하는 것이 아니라, 덩어리만 구하는 것으로 dfs/bfs 둘 다 가능
from collections import deque

T = int(input())

# 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0 # 현재 방문 처리

    while queue:
        now_x, now_y = queue.popleft()

        for i in range(4):
            nx, ny = now_x + dx[i], now_y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))


for _ in range(T):
    n, m, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]

    # 배추 위치 받기
    for _ in range(k):
        i, j = map(int, input().split())
        graph[i][j] = 1
    # print(graph)

    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i, j)
                count += 1

    print(count)