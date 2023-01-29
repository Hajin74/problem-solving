class Solution :
    def d(n) :
        sum = n
        while n > 0 :
            sum += n % 10
            n //= 10
        return sum

    not_self_number_list = []
    for i in range(1, 10001):
        not_self_number_list.append(d(i))
    
    for i in range(1, 10001):
        if i not in not_self_number_list:
            print(i)


    
    