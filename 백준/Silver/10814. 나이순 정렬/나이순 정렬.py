n = int(input())
# members = [list(input().split()) for _ in range(n)]
members = []
for _ in range(n):
    age, name = input().split()
    members.append([int(age),name])

members = sorted(members, key=lambda x: x[0])
for age, name in members:
    print(age, name)
