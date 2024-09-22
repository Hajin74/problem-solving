n = int(input())
s = str(n)

# 자릿수 구하기
count = 1 
while n >= 10:
    count += 1
    n //= 10

middle_index = int(count / 2)

# 반으로 나누기
s_list = list(s)
left_list = list(map(int, s_list[0:middle_index]))
right_list = list(map(int, s_list[middle_index:]))

# 자릿수 합 구하기
left_sum = sum(left_list)
right_sum = sum(right_list)

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")