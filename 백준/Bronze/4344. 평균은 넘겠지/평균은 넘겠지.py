class Solution :
    C = int(input())

    for i in range(C):
        scores = list(map(int, input().split()))
        scores.pop(0)

        count = 0
        for j in scores:
            if j > (sum(scores) / len(scores)):
                count += 1

        print('{:.3f}%' .format((count / len(scores) * 100)))

