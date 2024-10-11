# 나눠줄 수 있는 최대의 예산을 찾아라
# 1 <= 최대의 예산 <= 최대의 요청예산

n = int(input()) # 지방 수
requests = list(map(int, input().split())) # 각 지방의 요청예산들
requests.sort()
total_budget = int(input()) # 총 예산

start = 1
end = requests[-1]
max_budget = 1

while start <= end:
    mid = (start + end) // 2

    sum = 0
    for request in requests:
        if mid < request:
            sum += mid
        else:
            sum += request
    
    if sum <= total_budget:
        max_budget = max(max_budget, mid)
        start = mid + 1
    else:
        end = mid - 1

print(max_budget)