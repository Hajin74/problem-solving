class Solution :
    N = int(input())

    count = 0
    for i in range(1, N + 1):
        digit_list = list(map(int, str(i)))
        # print(digit_list)

        if i < 100 :
            count += 1
        elif digit_list[0] - digit_list[1] == digit_list[1] - digit_list[2] :
            # N은 100보다 작으니까 3자리수밖에 없음
            count += 1

    print(count)