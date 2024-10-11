# 0 <= h <= 1000000000
# 필요한 m미터 나무를 가져가기 위해 절단기에 설정할 최대의 높이 h를 구하라
# 적절한 h를 선택하는 것이 핵심
# 1부터 최대의 나무 높이까지 탐색하면서 찾아도되지만 시간이 오래걸리니 이분탐색으로 찾아보자

n, m = map(int, input().split()) # 주어진 나무 수, 필요한 나무 길이
trees = list(map(int, input().split()))

start = 0
end = max(trees)

while start <= end:
    mid = (start + end) // 2

    meter = 0
    for tree in trees:
        # 자를 수 있는 높이가 되는 나무만 자르기
        if tree >= mid:
            meter = meter + (tree - mid)
    
    # 나무가 부족하면 더 낮게 잘라야해
    if meter < m:
        end = mid - 1
    # 나무가 충분하면 더 높은 곳에서 자를 있는지 시도
    else:
        start = mid + 1

print(end)