n, m = map(int, input().split())
list = list(map(int, input().split()))

start = 0
end = max(list)

result = 0
while start <= end:
  total = 0
  mid = (start + end) // 2
  for tree in list:
    if tree > mid:
      total += tree - mid
  if total < m :
    end = mid - 1
  else:
    result = mid
    start = mid + 1

print(result)
