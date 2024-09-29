# x-1, x+1, 2x 갈 수 있는 위치가 인접한 노드가 된다
# 한 범위씩 넓혀가면서 k인 노드를 만나면 된다

from collections import deque

n, k = map(int, input().split())

def put_unvisited_node_on_queue(queue, n):
    for i in [n-1, n+1, n*2]:
        if 0 <= i <= 100000 and visited[i] == 0:
            queue.append(i)
            visited[i] = visited[n] + 1

visited = [0] * 100001

def bfs(n):
    if n > k:
        return n - k

    queue = deque()
    queue.append(n)

    while queue:
        now = queue.popleft()

        if now == k:
            return visited[now]
        
        put_unvisited_node_on_queue(queue, now)

print(bfs(n))