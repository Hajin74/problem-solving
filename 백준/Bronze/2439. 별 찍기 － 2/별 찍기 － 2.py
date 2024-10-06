n = int(input())

i = 1
while i <= n:
    empty = " " * (n-i)
    star = "*" * i
    line = empty + star
    print(line)
    i += 1