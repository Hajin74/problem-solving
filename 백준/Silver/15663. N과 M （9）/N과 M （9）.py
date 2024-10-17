import sys
input = sys.stdin.readline


def backtracking():
    if len(answer) == M:
        print(*answer)
        return
    
    same = 0
    for i in range(N):
        if not visited[i] and same != numbers[i]:
            visited[i] = True
            answer.append(numbers[i])
            same = numbers[i]

            backtracking()

            answer.pop()
            visited[i] = False


N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()

answer = []
visited = [False] * N

backtracking()