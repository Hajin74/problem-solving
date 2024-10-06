t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    result = a + b
    index = i + 1
    print(f"Case #{index}: {result}")
