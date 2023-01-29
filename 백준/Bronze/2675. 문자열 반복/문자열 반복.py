class Solution :
    T = int(input())
    for i in range(T):
        R, S = input().split()
        R = int(R)
        li = ''
        for s in S:
            li += R * s
        print(li)




    
    