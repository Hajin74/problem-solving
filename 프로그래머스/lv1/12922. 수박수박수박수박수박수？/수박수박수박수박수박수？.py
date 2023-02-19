def solution(n):
    word = ''
    for i in range(n):
        if i % 2 == 0:
            word += '수'
        else:
            word += '박'
    return word