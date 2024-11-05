def solution(my_string):
    answer = [int(str) for str in my_string if str.isdigit()]
    return sorted(answer)