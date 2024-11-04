def solution(bandage, health, attacks):
    current_health = health
    
    # 시간을 0초부터 공격의 마지막시간까지 1초씩 탐색하면서 체력을 계산한다
    # 공격은 오름차순으로 입력되므로 그대로 탐색하면 된다
    # 공격이 없는 시간에는 붕대감기 기술을 시전하여 체력을 회복하고
    # 공격이 있는 시간에는 공격 피해량 만큼 체력을 소진시킨다
    # 시전 시간만큼 붕대를 연속으로 감으면 추가 회복량만큼 체력을 회복한다
    
    last_attack_time = attacks[-1][0]
    attack_index = 0
    success_in_a_row_count = 0
    for time in range(1, last_attack_time + 1):
        if current_health <= 0:
            return -1
        
        if time == attacks[attack_index][0]: # 현재 시간에 공격이 있으면
            current_health -= attacks[attack_index][1] # 피해량만큼 체력을 소진시킨다
            success_in_a_row_count = 0 # 연속 성공 수 초기화
            attack_index += 1
        else: # 공격이 없으면
            current_health += bandage[1] # 초당 회복량만큼 체력을 회복한다
            success_in_a_row_count += 1 # 연속 성공수를 카운팅한다
            
            if success_in_a_row_count == bandage[0]: # 시전 시간만큼 연속 성공하면 
                current_health += bandage[2] # 추가 회복량만큼 체력을 회복한다
                success_in_a_row_count = 0  # 연속 성공 수 초기화
                
            if current_health >= health: # 최대 체력 이상의 체력을 가질 수 없다
                current_health = health
            
    if current_health <= 0:
        current_health = -1
        
    return current_health