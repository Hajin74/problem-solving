def solution(order):
    keys = ['3', '6', '9']
    count = 0
    for o in str(order):
        if o in keys:
            count += 1
    return count