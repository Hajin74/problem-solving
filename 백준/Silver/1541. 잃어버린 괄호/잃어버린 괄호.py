class Solution:
    exp = input().split('-')

    sum = 0

    # 0번째 원소 더하기
    for i in exp[0].split('+'):
        sum += int(i)

    # 나머지 원소들 다 빼기
    for i in exp[1:]:
        for j in i.split('+'):
            sum -= int(j)

    print(sum)