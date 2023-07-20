n, m = map(int, input().split())
snack = list(map(int, input().split()))
# print(snack)

start = 1
end = max(snack)

result = 0
while start <= end:
  mid = (start + end) // 2

  count = 0
  for item in snack:
    count += item // mid

  if count >= n:
    result = mid
    start = mid + 1
  else:
    end = mid - 1
    
print(result)