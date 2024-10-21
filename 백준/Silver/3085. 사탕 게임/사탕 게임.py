# 가능한 모든 경우 해보기
# 모든 칸에 인접한 칸을 탐색해서 다른 색이면 바꿔보고 사탕을 몇 개 먹을 수 있는지 기록

import sys
import copy

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def cal():
    global answer

    # 가장 긴 연속 행 카운팅
    for i in range(n):
        count = 1
        for j in range(n-1):
            if map[i][j] == map[i][j+1]:
                count += 1
                answer = max(answer, count)
            else:
                count = 1

    # 가장 긴 연속 열 카운팅
    for j in range(n):
        count = 1
        for i in range(n-1):
            if map[i][j] == map[i+1][j]:
                count += 1
                answer = max(answer, count)
            else:
                count = 1
            

n = int(input())
map = [list(input().rstrip()) for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(n - 1):
        map[i][j], map[i][j+1] = map[i][j+1], map[i][j] # 오른쪽과 스왑
        cal()
        map[i][j], map[i][j+1] = map[i][j+1], map[i][j] # 원상교체

        map[j][i], map[j+1][i] = map[j+1][i], map[j][i] # 아래쪽과 스왑
        cal()
        map[j][i], map[j+1][i] = map[j+1][i], map[j][i] # 원상교체


print(answer)