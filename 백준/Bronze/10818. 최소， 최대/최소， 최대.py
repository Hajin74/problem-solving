class Solution:
    N = int(input())
    nums = list(map(int, input().split()))
    min = max = nums[0]

    for i in nums:
        if i > max:
            max = i
        if i < min:
            min = i

    print(min, max, sep=' ')
    