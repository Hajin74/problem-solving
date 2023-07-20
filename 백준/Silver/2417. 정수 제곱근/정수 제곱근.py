n = int(input())

start = 1
end = n

result = 0
while start <= end:
  mid = (start + end) // 2
  if mid ** 2 == n:
    result = mid
    break
  elif mid ** 2 < n:
    start = mid + 1
  else:
    result = mid
    end = mid - 1


print(result)