T = int(input())

def calc(n):
    p = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

    if n > len(p):
        for i in range(10, n):
            p.append(p[-1] + p[i -5])

    return p[n - 1]


for i in range(T):
    n = int(input())
    print(calc(n))