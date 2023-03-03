def solution(n, k):
    drink =  k * 2000
    service = n // 10
    protein = n * 12000
    
    drink -= service * 2000
    if drink < 0:
        drink = 0
        
    total = protein + drink
    
    return total
    
    
   