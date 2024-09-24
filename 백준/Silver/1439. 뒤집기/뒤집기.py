S = input()

# 1과 0의 덩어리의 개수를 알아낸다
zero_count = 0
prev_c = '1'
for i in range(len(S)):
    if S[i] == '0':
        if prev_c == '1':
            prev_c = '0'
            zero_count += 1
    elif S[i] == '1':
        prev_c = '1'
# print(zero_count)

one_count = 0
prev_c = '0'
for i in range(len(S)):
    if S[i] == '1':
        if prev_c == '0':
            prev_c = '1'
            one_count += 1
    elif S[i] == '0':
        prev_c = '0'
# print(one_count)

# 많은 숫자로 덜 많은 숫자가 뒤집는다
result = 0
if zero_count > one_count:
    result += one_count
else:
    result += zero_count

print(result)