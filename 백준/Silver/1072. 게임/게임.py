X, Y = map(int, input().split())
Z = int(Y*100)//X
# print(Z)

start = 1
end = 1000000000
result = -1

if Z >= 99:
  print(result)
else:
  while start <= end:
    mid = (start + end) // 2
    x = X + mid
    y = Y + mid
    z = int(y*100)//x
  
    if z > Z:
      result = mid
      end = mid - 1
    else:
      start = mid + 1

  print(result)  