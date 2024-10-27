def solution(n, times):
    times.sort()
    
    answer = 0
    start = times[0]
    end = times[-1] * n
    
    while start <= end:
        mid = (start + end) // 2
        
        done = 0
        for time in times:
            done += mid // time
            
        if done < n:
            start = mid + 1
        else:
            answer = mid
            end = mid - 1
    
    return answer