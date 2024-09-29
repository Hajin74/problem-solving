# 갈 수 있는 방향들을 탐색
# 방문을 안했으면 방문해서 방문한 횟수 기록
# 해당 방문할 때의 횟수가 더 적으면 그 횟수로 변경
# 다음 방문 칸 내용 = 전의 방문 칸의 횟수 + 1
from collections import deque

t = int(input())

# 체스가 갈 수 있는 방향들
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[start_x][start_y] = 0

    while queue:
        now_x, now_y = queue.popleft()
        
        # 주위 탐색
        for i in range(8):
            nx, ny = now_x + dx[i], now_y + dy[i]
            
            # 범위 제한
            if nx < 0 or ny < 0 or nx >= l or ny >= l:
                continue
            
            # 방문 안했으면
            if graph[nx][ny] == -1:
                graph[nx][ny] = graph[now_x][now_y] + 1 # 지금 위치로부터 +1 기록으로 방문처리
                queue.append((nx, ny)) # 큐에 넣기

            # 더 짧은 방문으로 변경
            if graph[nx][ny] == graph[now_x][now_y] + 2:
                graph[nx][ny] = graph[now_x][now_y] + 1 # 지금 위치로부터 +1 기록으로 방문처리
                queue.append((nx, ny)) # 큐에 넣기

for _ in range(t):
    l = int(input()) # 체스판 길이 (l * l)
    graph = [[-1] * l for _ in range(l)]

    # 출발지와 도착지
    start_x, start_y = map(int, input().split())
    des_x, des_y = map(int, input().split())

    bfs(start_x, start_y)
    print(graph[des_x][des_y])