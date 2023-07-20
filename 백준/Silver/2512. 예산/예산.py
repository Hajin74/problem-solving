N = int(input())
array = list(map(int, input().split()))
# cut = array.copy()
budget = int(input())

if sum(array) <= budget:
  print(max(array))
else:
  start = 1
  end = max(array)

  result = 0
  while start <= end:
    mid = (start + end) // 2
    total = 0

    cut = []
    for item in array:
      if item > mid:
        cut.append(mid)
        total += mid
      else:
        cut.append(item)
        total += item
      
    if total > budget:
      end = mid - 1
    else:
      result = max(cut)
      start = mid + 1
      
  print(result)
    