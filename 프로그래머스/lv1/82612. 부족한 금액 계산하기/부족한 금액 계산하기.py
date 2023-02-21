def solution(price, money, count):
    result = money
    for i in range(1, count + 1):
        result -= price * i
    if result < 0:
        return -result
    else:
        return 0