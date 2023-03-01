import sys

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    ps = list(input().rstrip())

    stack = []
    for i in ps:
        if i == '(':
            stack.append(i)
        elif i == ')' and len(stack) > 0:
            stack.pop()
        elif len(stack) == 0 and i == ')':
            stack.append(i)
            break

    if len(stack) == 0:
        print("YES")
    else:
        print("NO")

