class Solution : 
    n = int(input())
    time = list(map(int, input().split()))
    time.sort()

    sum = 0
    min_sum = 0
    for i in time:
        sum += i
        min_sum += sum
    
    print(min_sum)