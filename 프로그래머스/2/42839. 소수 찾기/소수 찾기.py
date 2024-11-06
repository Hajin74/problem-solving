from itertools import permutations

def solution(numbers):
    numbers = list(numbers)

    temp = []
    for i in range(1, len(numbers) + 1):
        temp += list(permutations(numbers, i))
        
    num_set = set([int(''.join(t)) for t in temp])
    
    answer = 0
    for number in num_set :
        if is_prime_number(number):
            answer += 1
    
    return answer
        

def is_prime_number(number):
    if number == 0 or number == 1:
        return 0
    
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return 0
    return 1