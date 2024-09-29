# dfs로도 풀어보자

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

def dfs(graph, v, depth):
    for i in graph[v]:
        if depth[i] == -1:
            depth[i] = depth[v] + 1
            dfs(graph, i, depth)

# 출발지 x = 0, 출발지로 부터 방문 기록 +1
depth = [-1 for _ in range(n+1)]
depth[a] += 1
dfs(graph, a, depth)
# print(depth)
print(depth[b])
