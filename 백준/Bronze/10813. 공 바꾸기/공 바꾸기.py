n, m = map(int, input().split())

buckets = [0] * n
for i in range(n):
    buckets[i] = i+1

for j in range(m):
    x, y = map(int, input().split())
    temp = buckets[x-1]
    buckets[x-1] = buckets[y-1]
    buckets[y-1] = temp

print(*buckets)