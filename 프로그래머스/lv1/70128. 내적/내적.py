def solution(a, b):
    result = 0
    for x, y in zip(a, b):
        result += x * y
    return result