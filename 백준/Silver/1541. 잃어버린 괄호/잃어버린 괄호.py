expression = input()

arr = expression.split('-')

result = 0
temp = arr[0].split('+')
for j in temp:
        result += int(j)

for i in range(1, len(arr)):
    temp = arr[i].split('+')
    for j in temp:
        result -= int(j)
print(result)
