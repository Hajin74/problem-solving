import sys
import copy

sys.setrecursionlimit(10**6)
n  = int(input())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(graph, x, y):
    graph[x][y] = 0

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

        if graph[nx][ny] != 0:
            dfs(graph, nx, ny)


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
                dfs(under_graph, i, j)
                count += 1
    areas.append(count)

print(max(areas))