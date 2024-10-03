# i번째까지의 개수 = (i-1번째까지의 개수 + 1) + (i-2번째까지의 개수 + 1)
n = int(input())

dp = [0] * 1001 # n <= 1000
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[n])