def solution(arr, divisor):
    answer = list(filter(lambda x : x % divisor == 0, arr))
    
    if len(answer) == 0:
        return [-1]
    else:
        return sorted(answer)
  