from sys import stdin
input = stdin.readline
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int,input()[:-1].split())) for _ in range(M)]
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]
queue = deque()

for j in range(N):
    for i in range(M):
        if arr[i][j] == 1:
            queue.append((i,j))

while queue:
    this_x, this_y = queue.popleft()
    for ddx, ddy in zip(dx, dy):
        x, y = this_x + ddx, this_y + ddy
        if 0 <= x < M and 0 <= y < N:
            if arr[x][y] == 0:
                arr[x][y] = arr[this_x][this_y] + 1
                queue.append((x, y))

answer = 0
for i in range(M):
    for j in range(N):
        answer = max(answer, arr[i][j])
        if arr[i][j] == 0:
            print(-1)
            exit(0)

print(answer - 1)