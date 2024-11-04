def solution(video_len, pos, op_start, op_end, commands):
    # video_len, pos, op_start, op_end =  "10:55", "00:15", "00:15", "06:55"
    # commands =  ["next"]
    
    answer = ''
    
    pos = pos.split(':')
    pos_m = int(pos[0])
    pos_s = int(pos[1])
    # print(pos_m, pos_s)
    
    for cmd in commands:
        print("현재 위치:", pos_m, pos_s)
        
        op_start_m = int(op_start.split(':')[0])
        op_start_s = int(op_start.split(':')[1])
        print("오프닝 시작 위치:", op_start_m, op_start_s)
        
        op_end_m = int(op_end.split(':')[0])
        op_end_s = int(op_end.split(':')[1])
        print("오프닝 끝 위치:", op_end_m, op_end_s)
        
        # 현재 위치가 오프닝 구간일 경우
        if (pos_m == op_start_m and pos_s >= op_start_s) or (pos_m > op_start_m): # 오프닝 시작 위치보다 같거나 크고
            if (pos_m == op_end_m and pos_s <= op_end_s) or (pos_m < op_end_m) :# 오프닝 끝 위치보다 같거나 작으면
                pos_m = op_end_m
                pos_s = op_end_s
                print("바뀐 현재 위치:", pos_m, pos_s)
              
        # 현재 명령이 prev 라면, 10초 전으로 이동한다
        if cmd == 'prev':
            if pos_s >= 10:
                pos_s -= 10
            else:
                pos_m -= 1
                pos_s = 60 - (10 - pos_s)
        
        # 현재 명령이 next 라면, 10초 후으로 이동한다
        if cmd == 'next':
            if pos_s < 50:
                pos_s += 10
            else:
                pos_m += 1
                pos_s = 10 - (60 - pos_s)
                
        # 바뀐 위치가 오프닝 구간일 경우
        if (pos_m == op_start_m and pos_s >= op_start_s) or (pos_m > op_start_m): # 오프닝 시작 위치보다 같거나 크고
            if (pos_m == op_end_m and pos_s <= op_end_s) or (pos_m < op_end_m) :# 오프닝 끝 위치보다 같거나 작으면
                pos_m = op_end_m
                pos_s = op_end_s
                print("바뀐 현재 위치:", pos_m, pos_s)
        
        # 바뀐 시간이 00:00 보다 작으면 비디오 시작 시간으로 갱신한다
        if (pos_m == 0 and pos_s < 0) or pos_m < 0:
            pos_m = 0
            pos_s = 0
        
        # 바뀐 시간이 비디오 길이보다 크면 비디오 끝 시간으로 갱신한다
        video_len_m = int(video_len.split(':')[0])
        video_len_s = int(video_len.split(':')[1])
        if pos_m >= video_len_m and pos_s >= video_len_s:
            pos_m = video_len_m
            pos_s = video_len_s
        
        print()
        
    
    # 문자열 형식 따르기
    if pos_m == 0:
        pos_m = '00'
    elif pos_m < 10:
        pos_m = '0' + str(pos_m)
        
    if pos_s == 0:
        pos_s = '00'  
    elif pos_s < 10:
        pos_s = '0' + str(pos_s)
        
    pos_m = str(pos_m)
    pos_s = str(pos_s)
    
    answer = pos_m + ":" + pos_s
    print("최종 위치: ", answer) 
    
    return answer