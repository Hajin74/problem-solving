import re

def solution(my_string):
    numbers = re.sub(r'[^0-9]', '', my_string)
    count = 0
    for number in numbers:
        count += int(number)
    return count
        
    