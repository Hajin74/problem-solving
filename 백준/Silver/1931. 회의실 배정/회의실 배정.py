# 제일 빨리 끝나는 회의 선택
# 이전 회의 끝나는 시간 <= 현재 회의 시작 시간

import sys

n = int(input())

end_time = 0
count = 0

meetings = []
for i in range(0, n):
    a, b = map(int, sys.stdin.readline().split())
    meetings.append((a, b))
meetings.sort(key = lambda x : (x[1], x[0])) # 끝나는 시간으로 정렬, 그리고 시작하는 시간으로 정렬

for start, end in meetings:
    if end_time <= start: # 이전 회의 끝나는 시간 <= 현재 회의 시작 시간
        count += 1
        end_time = end

print(count)