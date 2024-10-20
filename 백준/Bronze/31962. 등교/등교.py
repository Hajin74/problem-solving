N, X = map(int, input().split()) # 버스 개수, X분 이내로 도착해야함

list = []
latest = -1
for i in range(N):
    S, T = map(int, input().split())
    time = S + T

    if time <= X:
        list.append((S, T))

        if i == 0:
            latest = S
        elif S > latest:
            latest = S


print(latest)