import sys

n = int(sys.stdin.readline())
nums = []
for i in range(n):
    a = int(sys.stdin.readline())
    nums.append(a)
nums.sort()

for i in nums:
    print(i)