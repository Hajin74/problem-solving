# 주변 노드들을 탐색해서 몇 번의 이동으로 도착했는지 기록
# bfs로 주변에 있는 것부터 기록
# 해당하는 도드의 이동횟수 출력

from collections import deque

n = int(input()) # 사람 수
a, b = map(int, input().split()) # 촌수를 알고 싶은 사람 번호
k = int(input()) # 관계 수

# 촌수 연결하기
graph = [[] for _ in range(n+1)] 
for _ in range(k):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)
#print(graph)

def bfs(graph, v, depth):
    queue = deque()
    queue.append(v)
    depth[v] += 1 # 출발지 0으로 초기화

    while queue:
        now = queue.popleft()

        for i in graph[now]:
            # 방문 안했으면 전에 있던 곳으로 부터 +1
            if depth[i] == -1:
                depth[i] = depth[now] + 1
                queue.append(i)

# 출발지 x = 0, 출발지로 부터 방문 기록 +1
depth = [-1 for _ in range(n+1)]
bfs(graph, a, depth)
print(depth[b])