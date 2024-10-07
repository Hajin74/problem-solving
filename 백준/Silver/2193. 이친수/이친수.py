# 0으로 시작하지 않는다
# 1이 두 번 연속으로 나타나지 않는다

n = int(input())

# dp[i] = 이친수의 개수
# dp[i] = dp[i-1] + dp[i-2]

dp = [0] * 91
dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])