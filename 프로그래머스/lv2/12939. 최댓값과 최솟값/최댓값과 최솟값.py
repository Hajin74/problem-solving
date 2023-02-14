def solution(s):
    li = list(map(int, s.split(" ")))
    result = str(min(li)) + " " + str(max(li))
    
    return result