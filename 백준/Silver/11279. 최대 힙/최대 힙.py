import heapq
import sys

N = int(sys.stdin.readline())

hq = []
for i in range(N):
    num = int(sys.stdin.readline())

    if num == 0:
        if len(hq) == 0:
            print(0)
        else:
            print(-heapq.heappop(hq))
        continue

    heapq.heappush(hq, -num)