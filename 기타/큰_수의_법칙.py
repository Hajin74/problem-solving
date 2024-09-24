n, m, k = map(int, input().split()) # 배열 크기, 더할 횟수, 연속 제한 횟수
li = list(map(int, input().split()))

li.sort(reverse=True) # 큰 수부터 정렬
first = li[0]
second = li[1]

# 가장 큰 수가 더해지는 횟수
count = int(m / (k+1)) * k # 더할 횟수 / 반복되는 수열의 길이 * 연속 제한 횟수
count += m % (k+1) # 딱 떨어지지 않는다면 나머지만큼 횟수가 더해진다

result = 0
result += (count) * first
result += (m-count) * second

print(result)