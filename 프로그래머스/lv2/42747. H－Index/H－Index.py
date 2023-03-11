def solution(citations):
    # citations.sort()
    
    h = 0
    for i in range(1, len(citations) + 1): 
        if sum(c >= i for c in citations) >= i:
            h = i

    return h