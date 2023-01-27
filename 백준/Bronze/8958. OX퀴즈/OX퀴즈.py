class Solution :
    n = int(input())
    

    for i in range(n):
        test_case = input()
        sum = 0
        score = 0
        for i in test_case:
            if i == 'O':
                score += 1
                sum += score
            else :
                score = 0

        print(sum)

