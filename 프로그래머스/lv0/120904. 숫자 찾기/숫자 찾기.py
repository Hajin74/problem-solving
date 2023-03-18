def solution(num, k):
    li = list(str(num))
    
    for i in range(len(li)):
        if li[i] == str(k):
            return i + 1
    
    return -1
            