n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]
li = list(filter(lambda coin : coin <= k, coins))
li.reverse()

count = 0
for e in li:
    # print(k)
    count += k // e
    k %= e

print(count)
