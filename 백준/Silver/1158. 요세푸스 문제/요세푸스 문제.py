from collections import deque

n, k = map(int, input().split())

queue = deque([i for i in range(1, n+1)])
result = []

while queue:
    for i in range(k-1):
        queue.append(queue.popleft())

    result.append(queue.popleft())

result = str(result)
print(result.replace('[', '<').replace(']', '>'))