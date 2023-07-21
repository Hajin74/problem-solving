N, M = map(int, input().split())
time = list(map(int, input().split()))

start = max(time) # 제일 큰 강의 하나가 들어갈 수 있는 크기가 제일 작은 값
end = sum(time) # 모든 강의 들어갈 수 있는 크기가 제일 큰 값

result = 0
while start <= end:
  mid = (start + end) // 2 # 몇으로 끊어서 담을 수 있는지 탐색
  sum = 0   # 강의 시간
  count = 1 # 블루레이 개수
  
  for t in time:
    if sum + t > mid: # 강의 시간이 끊어담을 수 있는 시간보다 크면 다음 블루레이에 기록
      count += 1 
      sum = 0
    sum += t

  if count <= M:
    result = mid
    end = mid - 1
  else:
    start = mid + 1

print(result)
