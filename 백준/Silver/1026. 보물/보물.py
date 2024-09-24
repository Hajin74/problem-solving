n = int(input())

a_list = list(map(int, input().split()))
a_list.sort()
a_list.reverse()

b_list = list(map(int, input().split()))
b_list.sort()

result = 0
for i in range(n):
    result += a_list[i] * b_list[i]

print(result)
