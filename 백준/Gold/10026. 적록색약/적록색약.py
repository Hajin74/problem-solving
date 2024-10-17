from collections import deque
import sys
import copy

n = int(input())
map = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

# 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(map, x, y):    
    queue = deque()
    queue.append((x, y))
    cc = map[x][y] # 현재 컬러

    while queue:
        cx, cy = queue.popleft()
        
        # 인접 탐색
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            # 범위 제한
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            
            # 현재 노드와 인접 노드의 색갈이 같으면 방문 (덩어리로 묶기)
            if map[nx][ny] != 'V' and map[nx][ny] == cc:
                map[nx][ny] = 'V'
                queue.append((nx, ny))

non_red_green_blindness_count = 0
non_red_green_blindness_map = copy.deepcopy(map)
for i in range(n):
    for j in range(n):
        if non_red_green_blindness_map[i][j] != 'V':
            bfs(non_red_green_blindness_map, i, j)
            non_red_green_blindness_count += 1
print(non_red_green_blindness_count)

red_green_blindness_count = 0
red_green_blindness_map = copy.deepcopy(map)

for i in range(n):
    for j in range(n):
        # 빨강과 초록을 같은 색으로 만들기
        if red_green_blindness_map[i][j] == 'R':
            red_green_blindness_map[i][j] = 'G'
for i in range(n):
    for j in range(n):
        if red_green_blindness_map[i][j] != 'V':
            bfs(red_green_blindness_map, i, j)
            red_green_blindness_count += 1
       
print(red_green_blindness_count)