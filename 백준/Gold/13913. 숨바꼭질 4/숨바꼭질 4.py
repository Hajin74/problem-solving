from collections import deque

N, K = map(int, input().split())

def bfs(n):
    queue = deque()
    queue.append(n)
    visited[n] = 0

    while queue:
        n = queue.popleft()
        
        if n == K:
            print(visited[n])
            return

        dx = [n-1, n+1, 2*n]
        for nx in dx:
            # 범위 제한
            if nx < 0 or nx > 100000:
                continue

            # 중복 방문 제한
            if visited[nx] == -1:
                queue.append(nx)
                visited[nx] = visited[n] + 1
                route[nx] = n

def print_route(n, move):
    path = []
    while True:
        if move == n:
            path.append(move)
            print(*reversed(path))
            return
        
        path.append(move)
        move = route[move]
        

route = [-1] * 100001 # 이전 위치 기록
visited = [-1] * 100001 # 방문 처리

bfs(N)
print_route(N, K)