T = int(input())

for t in range(T):
    k = int(input()) # 층
    n = int(input()) # 호

    dp = [[0] * n for _ in range(k+1)]
    for i in range(1, n+1):
        dp[0][i-1] = i

    for i in range(1, k+1):
        for j in range(n):
            for l in range(j+1):
                dp[i][j] += dp[i-1][l]

    print(dp[k][n-1])