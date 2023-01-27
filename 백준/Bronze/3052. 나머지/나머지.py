class Solution :
    nums = []
    for i in range(10):
        nums.append(int(input()) % 42)

    s = set(nums)

    print(len(s))