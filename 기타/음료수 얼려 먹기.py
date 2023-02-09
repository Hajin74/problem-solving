n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1

        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)

        return True

    return False


# 모든 노드를 다 돌면서 해당 노드에 상하좌우를 확인
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result)
