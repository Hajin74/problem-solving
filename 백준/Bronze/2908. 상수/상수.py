class Solution : 
    a, b = map(int, input().split())
    
    def reverse_number(n):
        sum = 0
        while n > 0 :
            sum = sum * 10 + n % 10
            n //= 10
        return sum

    print(max(reverse_number(a), reverse_number(b)))
    

