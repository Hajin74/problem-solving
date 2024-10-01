n = int(input())

size = []
ranking = []

for i in range(n):
    weight, height = map(int, input().split())
    size.append((weight, height))

for i in range(n):
    count = 1
    for j in range(n):
        if size[j][0] > size[i][0] and size[j][1] > size[i][1]:
            count += 1
    ranking.append(count)

print(*ranking)