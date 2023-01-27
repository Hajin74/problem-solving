class Solution:
    student = [0 for i in range(30)]

    for i in range(28):
        n = int(input())
        student[n - 1] = 1

    for i, ele in enumerate(student):
        if ele == 0:
            print(i + 1)