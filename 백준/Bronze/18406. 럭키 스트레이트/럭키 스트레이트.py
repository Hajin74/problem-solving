arr = input()
left = 0
right = 0

middle_index = len(arr) // 2
for i in range(middle_index):
    left += int(arr[i])
    right += int(arr[middle_index + i])

if left == right:
    print('LUCKY')
else:
    print('READY')