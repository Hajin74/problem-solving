class MySolution:
    n, m, k = map(int, input().split())
    nums = list(map(int, input().split()))

    sum = 0
    count = 0
    i = 0
    for i in range(m):
        if count < k:
            sum += max(nums)
            count += 1
        else:
            count = 0
            temp_nums = nums.copy()
            temp_nums.remove(max(nums))
            sum += max(temp_nums)
    
    print(sum)

class BookSolution:
    n, m, k = map(int, input().split())
    data = list(map(int, input().split()))

    data.sort()
    first_max = data[n - 1] 
    second_max = data[n - 2]

    # 가장 큰 수가 더해지는 횟수
    max_count = int(m / (k + 1)) * k
    max_count += m % (k + 1)

    result = 0
    result += max_count * first_max # 가장 큰 수 더하기
    result += (m - max_count) * second_max # 두 번째로 큰 수 더하기

    print(result)
