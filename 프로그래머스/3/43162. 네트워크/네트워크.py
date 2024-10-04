from collections import deque

def solution(n, computers):    
    # 연결리스트 만들기
    graph = [[] for _ in range(n+1)] 
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                graph[i+1].append(j+1)
    
    # bfs
    visited = [False] * (n+1)
    count = 0
    for c in range(1, n+1):
        if not visited[c]:
            bfs(graph, c, visited)
            count += 1
            
    return count

def bfs(graph, c, visited):
    queue = deque()
    queue.append(c)
    
    while queue:
        x = queue.popleft()

        # 인접한 노드 탐색
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)