n = int(input()) # n = 수의 길이, m = 시작 수
 
dp = [[0] * 11 for _ in range(n+1)]

# dp[1][m] = 1
for m in range(10):
    dp[1][m] = 1

# dp[n][m] = dp[n-1][0] + dp[n-1][1] + dp[n-1][2] + dp[n-1][3] + dp[n-1][m-2] + dp[n-1][m-1] + dp[n-1][m]
for i in range(2, n+1):
    for j in range(10):
        for k in range(j, 10):
            dp[i][j] += dp[i-1][k]

print(sum(dp[n]) % 10007)