def solution(x, n):
    answer = [x]
    current = x
    for i in range(1, n):
        current += x
        answer.append(current)
    
    return answer