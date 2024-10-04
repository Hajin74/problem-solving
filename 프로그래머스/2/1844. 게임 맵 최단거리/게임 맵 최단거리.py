# bfs 최단거리
from collections import deque

def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    x, y = 0, 0
    n, m = len(maps), len(maps[0])
    
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        
        # 주위 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # 범위 제한
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
                
            # 인접하면 방문처리하고, 큐에 넣기
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
    
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]