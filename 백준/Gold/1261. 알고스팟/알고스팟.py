from collections import deque

M, N = map(int, input().split())

maze = []
for _ in range(N):
    maze.append(list(map(int, input())))
# print(maze)

wall_break = [[-1] * M for _ in range(N)] 

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(a, b):
    queue = deque()
    queue.append([a, b])
    wall_break[0][0] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 이동 범위를 미로로 제한
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if wall_break[nx][ny] == -1:
                if maze[nx][ny] == 0:
                    wall_break[nx][ny] = wall_break[x][y] 
                    queue.appendleft([nx, ny]) # 벽이 없는 곳을 우선적으로 돌게, 큐의 앞에 넣어준다
                else:
                    wall_break[nx][ny] = wall_break[x][y] + 1
                    queue.append([nx, ny])

bfs(0, 0)
# print(maze)
print(wall_break[N-1][M-1])