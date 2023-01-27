class Solution :
    h, m = map(int, input().split())
    time = int(input())

    a = (m + time) // 60
    b = (m + time) % 60

    if m + time >= 60 :
        if h + a >= 24 :
            h = h - 24
        h += a
        print(h, b)
    else :
        if h >= 24 :
            h -= 24
        print(h, m + time)


    
