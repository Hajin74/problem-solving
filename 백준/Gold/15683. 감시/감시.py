import sys
import copy

input = sys.stdin.readline

# cctv 방향 (1번: [[상],[우],[하],[좌]], 2번: [[상,하],[우,좌]] ...)
direction = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]], 
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]]
]

# 방향: 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def fill(board, dir, x, y):
    for i in dir:
        nx = x
        ny = y

        while True:
            nx += dx[i]
            ny += dy[i]

            # 범위 제한
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                break

            if board[nx][ny] == 6: # 벽 만나면
                break
            
            # 방문 처리
            if board[nx][ny] == 0:
                board[nx][ny] = 7


def dfs(depth, office):
    global min_value

    if depth == len(cctv): # 모든 cctv를 다 탐색했을 때
        count = 0
        for i in range(N):
            count += office[i].count(0) # 행마다 사각지대 개수 카운팅
        min_value = min(min_value, count) # 최소 사각지대 갱신
        return 
    
    temp_board = copy.deepcopy(office) # cctv 하나당 보드 하나
    cctv_num, x, y = cctv[depth]
    for dir in direction[cctv_num]: # n번 cctv의 방향 모두 탐색
        fill(temp_board, dir, x, y) # cctv가 찍는 부분 채우기 (map, 방향, cctv 좌표)
        dfs(depth + 1, temp_board)
        temp_board = copy.deepcopy(office)


N, M = map(int, input().split())
office = []
cctv = []
for i in range(N):
    data = list(map(int, input().split()))
    office.append(data)
    for j in range(len(data)):
        if data[j] in [1, 2, 3, 4, 5]:
            cctv.append([data[j], i, j])

min_value = int(1e9)
dfs(0, office)
print(min_value)