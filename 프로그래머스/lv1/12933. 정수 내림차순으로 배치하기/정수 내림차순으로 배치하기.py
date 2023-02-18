def solution(n):
    li = list(str(n))
    li.sort(reverse = True)
    
    result = ''.join(li)
    return int(result)
    
