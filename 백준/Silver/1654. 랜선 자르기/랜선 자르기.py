k, n = map(int, input().split()) # 이미 가지고 있는 랜선 개수, 필요한 랜선 개수
lans = [int(input()) for _ in range(k)]

start = 1
end = max(lans)

while start <= end:
    mid = (start + end) // 2

    # 랜선 자르기
    count = 0
    for lan in lans:
        count += lan // mid
    # print("count:", count, "size:", mid)

    if count >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)