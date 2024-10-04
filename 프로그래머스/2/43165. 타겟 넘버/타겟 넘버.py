def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return count

count = 0
    
def dfs(numbers, target, curr_sum, idx):
    global count
    
    if idx == len(numbers):
        if curr_sum == target:
            count += 1
        return
    
    dfs(numbers, target, curr_sum + numbers[idx], idx + 1)
    dfs(numbers, target, curr_sum - numbers[idx], idx + 1)