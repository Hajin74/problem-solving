def solution(n):
    i = 1
    while True:
        if i ** 2 > n:
            return -1
        
        if n == i ** 2:
            return (i + 1) ** 2
        else :
            i += 1