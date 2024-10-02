n = int(input())

# i-1 은 1가지 (1*2)
# i-2 은 2가지 (1*2, 2*1 + 2*1)
# 따라서 i의 개수 = i-1의 개수 + i-2의 개수

dp = [0] * (n+1)
dp[0] = 1
dp[1] = 1

for i in range(2, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[n])