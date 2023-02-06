class MySolution:
    loc = input()

    x = int(loc[1])
    y = ord(loc[0]) - 96

    dx = [-2, -2, -1, 1, 2, 2, 1, -1]
    dy = [-1, 1, 2, 2, 1, -1, -2, -2]

    count = 0
    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 1 or ny < 1 or nx > 8 or ny > 8:
            continue
        else:
            count += 1

    print(count)

class BookSolution:
    input_data = input()
    row = int(input_data[1])
    col = int(ord(input_data[0])) - int(ord('a')) + 1

    steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

    result = 0
    for step in steps:
        next_row = row + step[0]
        next_col = col + step[1]

        if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
            result += 1

    print(result)