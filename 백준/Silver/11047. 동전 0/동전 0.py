class Solution : 
    n, k = map(int, input().split())

    coins = []
    for i in range(n):
        coins.append(int(input()))
    coins.sort(reverse=True)

    count = 0
    for i in coins:
        if i <= k :
            count += k // i
            k %= i
    
    print(count)