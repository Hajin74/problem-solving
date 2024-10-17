import sys

N, M = map(int, input().split())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()

answer = []

def bt():
    if len(answer) == M:
        print(*answer)
        return
    
    for num in numbers:
        answer.append(num)
        bt()
        answer.pop()

bt()