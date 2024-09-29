# 1부터 최대 높이까지 안전영역 개수를 구한다
# 안전영역의 개수가 가장 큰 걸 출력한다
# 비의 높이를 입력받아 해당 높이와 같거나 작은건 방문하지 못하게 한다
# 이 때, 안전영역은 방문할 수 있는 곳의 덩어리의 개수다

from collections import deque
import sys
import copy

n  = int(input())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0 # 방문처리

    while queue:
        curr_x, curr_y = queue.popleft()

        for i in range(4):
            nx, ny = curr_x + dx[i], curr_y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            # 비의 잠기지 않고 방문하지 않았으면
            if graph[nx][ny] != 0:
                graph[nx][ny] = 0
                queue.append((nx, ny))


# 비의 잠긴 부분 표시하기
def under_water(height):
    under_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(n):
            if under_graph[i][j] <= height:
                under_graph[i][j] = 0 # 잠김 처리
    return under_graph

# 최대 영역 찾기
max_height = max(map(max, graph))

areas = []
for k in range(max_height + 1):
    under_graph = under_water(k)
    count = 0
    for i in range(n):
        for j in range(n):
            if under_graph[i][j] != 0:
                bfs(under_graph, i, j)
                count += 1
    areas.append(count)

print(max(areas))