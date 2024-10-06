n = int(input())

i = 1
while i < n:
    empty = " " * (n-i)
    star = "*" * i
    left = star + empty
    right = empty + star
    print(left + right)
    i += 1

i = 0
while i < n:
    empty = " " * i
    star = "*" * (n - i)
    left = star + empty
    right = empty + star
    print(left + right)
    i += 1