import sys
input = sys.stdin.readline

n = int(input())
nums = set(map(int, input().split()))
nums = list(nums)
nums.sort()

for i in nums:
    print(i, end=" ")

