class Solution :
    pip1, pip2, pip3 = map(int, input().split())

    if pip1 == pip2 == pip3 :
        print(10000 + pip1 * 1000)
    elif pip1 != pip2 and pip2 != pip3 and pip1 != pip3 :
        print(max(pip1, pip2, pip3) * 100)
    else :
        if pip1 == pip2 :
            print(1000 + pip1 * 100)
        elif pip1 == pip3 :
            print(1000 + pip1 * 100)
        elif pip2 == pip3 :
            print(1000 + pip2 * 100)

    
