# 0과 1의 덩어리 개수 세기
# 많은 쪽으로 숫자 뒤집기
# 뒤집은 횟수 반환

S = input()

zero_count = 0
one_count = 0

for i in range(len(S) - 1):
    if S[i] != S[i+1]:
        if S[i] == '0':
            zero_count += 1
        elif S[i] == '1':
            one_count += 1

if S[len(S) - 1] == '0':
    zero_count +=1
else:
    one_count += 1

if zero_count < one_count:
    print(zero_count)
else:
    print(one_count)