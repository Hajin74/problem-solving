class Solution :
    N = int(input())
    num = N
    cycle = 0
    
    while True:
        num1 = num // 10
        num2 = num % 10
        sum = (num1 + num2) % 10
        num = (num2 * 10) + sum

        cycle += 1

        if num == N :
            break

    print(cycle)
        
    