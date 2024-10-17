import sys

n, s = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

def backtracking(start):
    global count

    if sum(answer) == s and len(answer) > 0:
        count += 1

    for i in range(start, n):
       answer.append(numbers[i])
       backtracking(i+1)
       answer.pop()

count = 0
answer = []

backtracking(0)

print(count)

