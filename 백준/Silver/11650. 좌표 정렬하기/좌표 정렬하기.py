import sys

input = sys.stdin.readline

n = int(input())
li = []
for i in range(n):
    x, y = map(int, input().split())
    li.append((x, y))

for t in sorted(li):
    print(t[0], t[1])