from collections import deque

def solution(n, computers):
    visited = [False] * n
    network = 0
    
    for i in range(n):
        if not visited[i]:
            bfs(i, computers, visited)
            network += 1
    
    return network

def bfs(start, computers, visited):
    queue = deque()
    queue.append(start)
    visited[start] = True
    
    while queue:
        now = queue.popleft()
        for i in range(len(computers[now])):
            if i != now and not visited[i] and computers[now][i] == 1:
                queue.append(i)
                visited[i] = True
                
    
    
    
    