class Solution :
    s = input()
    alphabet = [chr(i) for i in range(97, 123)]

    for i in alphabet :
        if i in s :
            print(s.index(i), end=' ')
        else :
            print(-1, end=' ')



    
    