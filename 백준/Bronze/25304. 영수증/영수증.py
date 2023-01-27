class Solution :
    total_price = int(input())
    total_count = int(input())
    
    sum = 0
    for i in range(total_count):
        price, count = map(int, input().split())
        sum += price * count

    if total_price == sum :
        print('Yes')
    else : 
        print('No')
    
