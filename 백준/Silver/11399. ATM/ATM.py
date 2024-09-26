# 빨리 끝나는 사람부터 인출해야함

n = int(input())
watings = list(map(int, input().split()))
watings.sort()

sum = 0
result = 0
for wating in watings:
    result += wating
    sum +=  result

print(sum)