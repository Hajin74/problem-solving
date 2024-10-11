# 정해진 공유기를 최대한 인접하지 않게 멀리멀리 설치하기

n, c = map(int, input().split())
homes = [int(input()) for _ in range(n)]
homes.sort()

# 최소거리, 최대거리
start = 1
end = homes[-1] - homes[0]

while start <= end:
    mid = (start + end) // 2

    current_home = homes[0]
    count = 1

    # 거리만 만족하면 더 넓히지 않고 카운팅
    for i in range(1, n):
        if homes[i] >= current_home + mid:
            count += 1
            current_home = homes[i]
    
    # 공유기가 다 설치될만큼의 거리이면, 거리를 더 넓힐 수 있는지 시도
    if count >= c:
        start = mid + 1
        result = mid # 현재 결과를 저장하자, 더 넓히지 못할 수도 있으니까, 이게 최선의 답일 수 있다
    else:
        end = mid - 1

print(result)