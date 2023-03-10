def solution(t, p):
    start = 0
    end = len(p)
    
    count = 0
    while end <= len(t):
        temp = int(t[start:end])
        if temp <= int(p):
            count += 1
        start += 1
        end += 1
    
    return count
    