n, m = map(int, input().split())

min_cards = [min(list(map(int, input().split()))) for _ in range(n)]
print(max(min_cards))
