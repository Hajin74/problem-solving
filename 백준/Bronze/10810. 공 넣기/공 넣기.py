# k번 공을 i번 ~ j번 바구니에 모두 넣어야함
# 바구니에는 공을 1개만 넣을 수 있음
# 바구니에 이미 공이 들어있으면 빼서, 새로운 공을 넣는다

n, m = map(int, input().split()) # 바구니 개수, 공을 넣을 횟수

buckets = [0] * (n+1) # 빈 바구니로 초기화

for _ in range(m):
    # i번 ~ j번 바구니까지, k번 공을 넣는다
    i, j, k = map(int, input().split()) 

    for b in range(i, j+1):
            buckets[b] = k

for b in range(1, n+1):
    print(buckets[b], end=' ')