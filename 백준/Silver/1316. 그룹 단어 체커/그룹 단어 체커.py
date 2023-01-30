class Solution : 
    n = int(input())
    
    count = 0
    for i in range(n) :
        flag = 1
        alpha_list = []
        word = input()
        for j in word :
            if j not in alpha_list :
                alpha_list.append(j)
            else :
                if j != prev_s :
                    flag = 0
                    break

            prev_s = j
        
        if flag == 1 :
            count += 1
            
    print(count)