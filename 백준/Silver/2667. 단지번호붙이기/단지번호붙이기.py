N = int(input())

graph = []
for i in range(N):
  graph.append(list(map(int, input())))

count = 0
def dfs(x, y):
  if x < 0 or x >= N or y < 0 or y >= N:
    return False

  if graph[x][y] == 1:
    global count
    count += 1
    
    graph[x][y] = 0
    dfs(x - 1, y)
    dfs(x + 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)

    return True

  return False


list = []
result = 0
for i in range(N):
  for j in range(N):
    if dfs(i, j) == True:
      list.append(count)
      count = 0
      result += 1

print(result)

for item in sorted(list):
  print(item)
