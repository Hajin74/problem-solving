import math

def solution(n, m):
    answer = []
    
    answer.append(math.gcd(n, m))
    answer.append(lcm(n, m))
    
    return answer

def lcm(a, b):
    return a * b / math.gcd(a, b)