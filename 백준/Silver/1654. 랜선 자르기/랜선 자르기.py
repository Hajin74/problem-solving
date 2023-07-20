n, m = map(int, input().split())
list = []
for _ in range(n):
  list.append(int(input()))

start = 1
end = max(list)

result = 0
while start <= end:
  total = 0
  mid = (start + end) // 2
    
  for item in list:
    total += item // mid
    
  if total < m:
    end = mid - 1
  else:
    result = mid
    start = mid + 1
    
print(result)
