import sys

n = int(input())
stack = []


def push(num):
    stack.append(num)


def pop():
    if len(stack) > 0:
        result = stack.pop()
    else:
        result = -1

    print(result)


def size():
    print(len(stack))


def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)


def top():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])


for i in range(n):
    order = list(map(str, sys.stdin.readline().split()))
    # print(order)
    if order[0] == 'push':
        push(int(order[1]))
    elif order[0] == 'top':
        top()
    elif order[0] == 'size':
        size()
    elif order[0] == 'empty':
        empty()
    elif order[0] == 'pop':
        pop()
