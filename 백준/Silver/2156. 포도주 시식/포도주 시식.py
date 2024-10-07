n = int(input())
arr = [int(input()) for _ in range(n)]

# dp[i] = i번째 먹었을 때 먹은 포도주 최대량
dp = [0] * n

if n == 1:
    print(arr[0])
elif n == 2:
    print(arr[0] + arr[1])
else:
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]

    for i in range(2, n):
        dp[i] = max(arr[i] + arr[i-1] + dp[i-3], arr[i] + dp[i-2], dp[i-1])

    print(max(dp))