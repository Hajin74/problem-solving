from itertools import combinations

def solution(numbers):
    answer = []
    combi = list(combinations(numbers, 2))
    for c in combi:
        if sum(c) not in answer:
            answer.append(sum(c))
    return sorted(answer)