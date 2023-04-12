def solution(before, after):
    for a in after:
        if a in before:
            before = before.replace(a, '*', 1)
        else:
            return 0
        
    return 1