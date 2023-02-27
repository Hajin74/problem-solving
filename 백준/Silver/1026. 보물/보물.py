import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

a.sort()
b.sort(reverse=True)

result = 0
for pair in zip(a, b):
    result += pair[0] * pair[1]

print(result)
