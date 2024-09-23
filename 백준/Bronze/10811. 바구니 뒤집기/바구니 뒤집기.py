n, m = map(int, input().split())
buckets = [i for i in range(1, n+1)]

def reverse_buckets(i, j):
    temp = buckets[i-1:j]
    temp.reverse()
    buckets[i-1:j] = temp

for _ in range(m):
    i, j = map(int, input().split())
    reverse_buckets(i, j)

print(*buckets)