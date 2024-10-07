import sys

n = int(sys.stdin.readline())

count = [0] * 10001 # 입력받을 수의 크기만큼

# 1은 몇 개, 2는 몇 개 이런식으로 기록

for _ in range(n):
    num = int(sys.stdin.readline())
    count[num] += 1

for i in range(1, 10001):
    # 기록된 만큼 출력하자
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)