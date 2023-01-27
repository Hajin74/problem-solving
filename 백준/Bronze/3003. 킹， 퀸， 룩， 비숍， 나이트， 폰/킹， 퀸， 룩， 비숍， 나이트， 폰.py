class Solution:
    count = [1, 1, 2, 2, 2, 8]
    white = list(map(int, input().split()))

    for i in range(len(count)):
        print(count[i] - white[i])
