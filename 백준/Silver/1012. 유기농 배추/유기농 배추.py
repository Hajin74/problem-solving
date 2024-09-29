# 이것도 최단경로를 구하는 것이 아니라, 덩어리만 구하는 것으로 dfs/bfs 둘 다 가능
import sys
sys.setrecursionlimit(10000)

T = int(input())

# 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):

    if x < 0 or y < 0 or x >= n or y >= m:
        return
    
    if graph[x][y] == 1:
        graph[x][y] = 0 # 현재 방문 처리

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            dfs(nx, ny)


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
                dfs(i, j)
                count += 1

    print(count)

