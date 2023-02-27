import sys

stack1 = list(sys.stdin.readline().rstrip())
stack2 = []

for _ in range(int(sys.stdin.readline())):
    order = list(sys.stdin.readline().split())

    if order[0] == 'L':
        if stack1:
            stack2.append(stack1.pop())
    elif order[0] == 'D':
        if stack2:
            stack1.append(stack2.pop())
    elif order[0] == 'B':
        if stack1:
            stack1.pop()
    else:
        stack1.append(order[1])
        
stack1.extend(reversed(stack2))
print(''.join(stack1))