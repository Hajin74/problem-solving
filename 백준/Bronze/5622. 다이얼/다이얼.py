class Solution : 
    dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    
    str = input()

    time = 0
    for i in str :
        for j in dial:
            if i in j:
                time += dial.index(j) + 3
    
    print(time)