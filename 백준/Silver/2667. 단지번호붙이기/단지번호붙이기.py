from collections import deque

n = int(input()) # 지도의 크기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append([x, y])

    # 첫번째 집 방문 처리
    graph[x][y] = 0
    count = 1 

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append([nx, ny])
                count += 1
    
    return count

result = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            count = bfs(i, j)
            result.append(count)
result.sort()

print(len(result))
for k in result:
    print(k)