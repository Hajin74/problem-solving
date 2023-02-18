def solution(numbers):
    remove_set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    
    for i in numbers:
        remove_set.remove(i)
        
    return sum(remove_set)