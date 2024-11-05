def solution(rsp):
    answer = ''
    
    for e in rsp:
        if e == '2':
            answer += '0'
        elif e == '0':
            answer += '5'
        else:
            answer += '2'
    
    return answer