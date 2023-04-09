def solution(my_string):
    list = ['a', 'e', 'i', 'o', 'u']
    answer = ''
    for str in my_string:
        if str not in list:
            answer += str
    return answer