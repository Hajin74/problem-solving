n = int(input())

members = []
for _ in range(n):
    name, korean, english, math = input().split()
    members.append([name, int(korean), int(english), int(math)])

members = sorted(members, key=lambda x: (-x[1], x[2], -x[3], x[0]))
for member in members:
    print(member[0])