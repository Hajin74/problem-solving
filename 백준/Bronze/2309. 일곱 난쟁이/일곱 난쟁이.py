import itertools

height = [int(input()) for _ in range(9)]

# 7명씩 선택하여 딱 100이 되나 가능한 모든 경우를 계산해보기

combs = itertools.combinations(height, 7)
for c in combs:
    if sum(c) == 100:
       result = sorted(list(c))
       print(*result)
       break