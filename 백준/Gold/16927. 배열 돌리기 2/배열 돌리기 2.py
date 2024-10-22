import sys
from collections import deque

# 1차원 배열로 느러뜨려서 회전하고 다시 2차원 배열로 만들자

n, m, r = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

answer = [[0] * m for _ in range(n)]
queue = deque()

loop = min(n, m) // 2 # 몇 겹으로 되어있는지, 작은 수의 절반 만큼 겹이 쌓임

for i in range(loop):
    queue.clear()

    # 2차원 배열을 1차원 배열로 느러뜨리기
    queue.extend(matrix[i][i:m-(i+1)]) # 윗줄
    queue.extend(row[m-(i+1)] for row in matrix[i:n-(i+1)]) # 오른줄
    queue.extend(matrix[n-(i+1)][m-(i+1):i:-1]) # 아랫줄
    queue.extend(row[i] for row in matrix[n-(i+1):i:-1]) # 왼줄

    queue.rotate(-r)

    # 1차원 배열을 다시 2차원 배열로 만들기
    for j in range(i, m-(i+1)): # 윗줄
        answer[i][j] = queue.popleft()

    for j in range(i, n-(i+1)): # 오른줄
        answer[j][m-(i+1)] = queue.popleft()

    for j in range(m-(i+1), i, -1): # 아랫줄
        answer[n-(i+1)][j] = queue.popleft()

    for j in range(n-(i+1), i, -1): # 왼줄
        answer[j][i] = queue.popleft()


for i in range(n):
    print(*answer[i])