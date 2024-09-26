import sys
input = sys.stdin.readline()

s = input.split('-')

temp = []
for i in s:
    sum = 0
    for j in i.split('+'):
        sum += int(j)
    temp.append(sum)

result = temp[0]
for i in temp[1:]:
    result -= i
    
print(result)    