n, m = map(int, input().split())

while n != 0 and m != 0:
    if m % n == 0:
        print("factor")
    elif n % m == 0:
        print("multiple")
    elif n != 0 and m != 0:
        print("neither")
    n, m = map(int, input().split())