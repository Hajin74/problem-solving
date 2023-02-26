import sys

n = int(sys.stdin.readline())
cards = set(map(int, input().split()))
m = int(sys.stdin.readline())
tests = list(map(int, input().split()))

result = ['0'] * m
for i in range(m):
    if tests[i] in cards:
        result[i] = '1'

print(" ".join(result))