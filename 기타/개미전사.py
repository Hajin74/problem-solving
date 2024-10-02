n = int(input())
stores = list(map(int, input().split()))

# 현재 위치한 i번째 창고 + 한 칸 이상 떨어진 i-2번째 창고를 털 것이냐
# 현재 창고 옆에 붙어있는 i-1번째 창고를 털 것이냐
# 그 중에 큰 걸 털어야겠지

dp = [0] * n # n <= 100

# i번째까지의 최적의 해를 찾아나가자
# 바텀업
dp[0] = stores[0]
dp[1] = max(stores[0], stores[1])
for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2] + stores[i])

print(dp)