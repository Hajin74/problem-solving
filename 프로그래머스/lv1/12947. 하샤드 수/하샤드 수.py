def solution(x):
    nums = list(map(int, str(x)))
    
    if x % sum(nums) == 0:
        return True
    else:
        return False
    