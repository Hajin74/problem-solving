n = int(input())
pos = [list(map(int, input().split())) for _ in range(n)]

pos = sorted(pos, key=lambda x: (x[1], x[0]))
for x, y in pos:
    print(x, y)