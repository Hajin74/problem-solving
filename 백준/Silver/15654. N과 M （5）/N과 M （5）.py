import sys

N, M = map(int, input().split())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()

answer = []

def backtracking():
    if len(answer) == M:
        print(" ".join(map(str, answer)))
        return
    
    for num in numbers:
        if num not in answer:
            answer.append(num)
            backtracking()
            answer.pop()

backtracking()