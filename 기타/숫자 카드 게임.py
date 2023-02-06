class MySolution:
    n, m = map(int, input().split())

    mins = []
    for i in range(n):
        cards = list(map(int, input().split()))
        mins.append(min(cards))

    print(max(mins))
    
