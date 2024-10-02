# 동전끼리 배수가 아니기 때문에 그리디가 안된다
# 적은 금액부터 큰 금액까지 확인하며, 차례대로 만들 수 있는 최소한의 화폐 개수를 찾아야함

n, m = map(int, input().split())

coins = [] # 화폐 단위 [2, 3, 5, 7]
for i in range(n):
    coins.append(int(input()))

d = [10001] * (m+1)

# 각 화폐 단위를 하나씩 확인한다
d[0] = 0
for i in range(n): # 화폐 개수만큼 돌기
    for j in range(coins[i], m+1): # 만들고 싶은 숫자만큼 돌기
        if d[j - coins[i]] != 10001: # 현재 인덱스 i - k(화폐 단위)을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - coins[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])