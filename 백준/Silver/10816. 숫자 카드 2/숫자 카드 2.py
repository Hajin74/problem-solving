import sys

input = sys.stdin.readline

n = int(input())
have_cards = list(map(int, input().split()))
m = int(input())
test_cards = list(map(int, input().split()))

count = dict()

for c in have_cards:
    if c in count:
        count[c] += 1
    else:
        count[c] = 1

for c in test_cards:
    if c in count:
        print(count[c], end=" ")
    else:
        print(0, end=" ")