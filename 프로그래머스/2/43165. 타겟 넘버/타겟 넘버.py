def solution(numbers, target):
    dfs(numbers, 0, 0, target)
    
    return answer

def dfs(numbers, sum, i, target):
    global answer
    
    if i == len(numbers):
        if sum == target:
            answer += 1
        return
    
    dfs(numbers, sum + numbers[i], i + 1, target)
    dfs(numbers, sum - numbers[i], i + 1, target)
  
answer = 0
