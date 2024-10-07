n = int(input())
arr = list(map(int, input().split()))
arr.sort()
t = int(input())
case = list(map(int, input().split()))

def bs(arr, key, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] == key:
            return 1
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1

    return 0

for key in case:
    result = bs(arr, key, 0, n-1)
    print(result)