n, c = map(int, input().split())
homes = []
for _ in range(n):
  homes.append(int(input()))
homes.sort()

start = 1
end = homes[-1] - homes[0]
result = 0

while start <= end:
  mid = (start + end) // 2
  current = homes[0]
  count = 1

  # 현재 위치의 집과 해당 집의 거리가 최소 거리를 지키는가
  for i in range(1, n):
    if homes[i] >= current + mid:
      count += 1
      current = homes[i]

  if count >= c:
    result = mid
    start = mid + 1
  else:
    end = mid - 1

print(result)
    