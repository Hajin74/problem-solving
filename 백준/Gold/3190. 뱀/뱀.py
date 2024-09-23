from collections import deque

# 큐로 뱀의 이동 좌표를 표현

n = int(input()) # 보드 크기
k = int(input()) # 사과 개수

graph = [[0] * n for _ in range(n)]

# 우하좌상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 사과는 보드에 2로 표시
for i in range(k):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 2

l = int(input())
dir_dict = dict()

queue = deque()
queue.append((0, 0))

# 초와 방향을 딕셔너리 형태로 저장
for i in range(l):
    second, dir = input().split()
    dir_dict[int(second)] = dir

# 방향 전환하기
def turn(c):
    global direction
    if c == 'L':
        direction = (direction - 1) % 4
    elif c == 'D':
        direction = (direction + 1) % 4

x, y = 0, 0
graph[x][y] = 1
direction = 0 # 현재는 뱀이 오른쪽을 향하고 있음
time = 0

while True:
    time += 1

    # 현재 향하고 있는 방향으로 1번 이동하면 나오는 좌표
    x += dx[direction]
    y += dy[direction]

    # 보드 범위 밖으로 나가면 종료
    if x < 0 or x >= n or y < 0 or y >= n:
        break

    # 사과를 만나면
    if graph[x][y] == 2:
        graph[x][y] = 1 # 뱀 지나간다고 표시
        queue.append((x, y)) # 머리 늘리기

        # 타이밍되면 방향 전환하기
        if time in dir_dict:
            turn(dir_dict[time])
    
    # 사과가 없으면
    elif graph[x][y] == 0:
        graph[x][y] = 1 # 뱀 지나간다고 표시
        queue.append((x, y)) # 머리 늘리기
        tail_x, tail_y = queue.popleft() # 꼬리 줄어들기
        graph[tail_x][tail_y] = 0 # 뱀 지나간 부분 0으로 초기화

        # 타이밍되면 방향 전환하기
        if time in dir_dict:
            turn(dir_dict[time])
    
    # 자기 몸일 경우
    else:
        break

print(time)