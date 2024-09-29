n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global count

    if x < 0 or y < 0 or x >= n or y >= n:
        return
    
    if graph[x][y] == 1:
        count += 1
        graph[x][y] = 0 

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)

    
count = 0
homes = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            dfs(i, j)
            homes.append(count)
            count = 0

homes.sort()
print(len(homes))
for home in homes:
    print(home)