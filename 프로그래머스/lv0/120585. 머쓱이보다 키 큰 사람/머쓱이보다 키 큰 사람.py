def solution(array, height):
    count = 0
    for h in array:
        if height < h:
            count += 1
    return count