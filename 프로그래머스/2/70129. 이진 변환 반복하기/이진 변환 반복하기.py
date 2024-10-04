def solution(s):
    zero_remove_count = 0
    transfer_count = 0
    
    x = s
    
    while x != '1':
        zero_remove_count += x.count('0')  # 0제거한 0의 개수
        x = x.replace('0', '') # 0제거
        c = len(x) # x의 길이

        x = bin(c).replace('0b', '') # c를 2진수로 변환
        transfer_count += 1
        
    return [transfer_count, zero_remove_count]
        
