kg = int(input())

# kg가 5로 나눠질 경우
# kg가 3과 5로 나눠질 경우
# kg가 3으로 나눠질 경우
# kg가 3과 5로 나눠지지 않을 경우

bag = 0
while kg >= 0:
    if kg % 5 == 0: # 5의 배수이면
        bag += kg // 5 # 몫 바로 출력
        print(bag) 
        break
    kg -= 3 # 5의 배수가 될 때까지, 설탕 -3 봉지 +1
    bag += 1 
else:
    print(-1)