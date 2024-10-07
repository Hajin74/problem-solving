n = int(input()) # n = 수의 길이, m = 마지막 수

dp = [[0] * 11 for _ in range(n+1)]

# dp[1][m] = 1
# dp[1][0] = 0, dp[1][10] = 0
for i in range(1, 10):
    dp[1][i] = 1

# dp[n][0] = dp[n-1][1]
# dp[n][m] = dp[n-1][m-1] + dp[n-1][m+1]
for i in range(2, n+1):
    dp[i][0] = dp[i-1][1]
    for j in range(1, 10):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n]) % 1000000000)