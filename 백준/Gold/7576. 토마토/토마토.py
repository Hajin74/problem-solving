# 하루에 인접한 곳을 한 단계 갈 수 있다
# 며칠만에 모든 토마토를 다 탐색할 수 있을지 구하면 된다 -> 최단경로
# 토마토가 모두 익지 못하면 -1 출력
# 익은 토마토: 1, 익지 않은 토마토: 0, 토마토 없음: -1

from collections import deque
import sys

m, n = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 익은 토마토 좌표 찾아서 방문할 좌표로 큐에 넣기
queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))

def bfs():
    while queue:
        now_x, now_y = queue.popleft()

        for i in range(4):
            nx, ny = now_x + dx[i], now_y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[now_x][now_y] + 1
                queue.append((nx, ny))

bfs()

isReap = True
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            isReap = False
            break

if isReap:
    max_value = max(map(max, graph)) - 1
    print(max_value)
else:
    print(-1)
