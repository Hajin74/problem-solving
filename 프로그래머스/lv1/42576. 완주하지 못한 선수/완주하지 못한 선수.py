def solution(participant, completion):
    dict = {}
    
    for p in participant:
        if p in dict:
            dict[p] += 1
        else: 
            dict[p] = 1
    
    for c in completion:
        if c in dict:
            dict[c] -= 1
            
    for key, value in dict.items():
        if value != 0:
            return key
