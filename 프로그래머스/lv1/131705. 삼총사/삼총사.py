from itertools import combinations

def solution(number):
    combi = list(combinations(number, 3))
    
    result = 0
    for i in combi:
        if sum(i) == 0:
            result += 1
    return result