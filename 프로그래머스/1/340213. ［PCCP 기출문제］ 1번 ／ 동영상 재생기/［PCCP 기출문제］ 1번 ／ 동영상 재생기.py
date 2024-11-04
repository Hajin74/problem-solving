def time_to_seconds(time_str):
    minutes, seconds = map(int, time_str.split(':'))
    return minutes * 60 + seconds

def seconds_to_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    return f"{minutes:02d}:{seconds:02d}"

def solution(video_len, pos, op_start, op_end, commands):
    video_len = time_to_seconds(video_len)
    curr_pos = time_to_seconds(pos)
    op_start = time_to_seconds(op_start)
    op_end = time_to_seconds(op_end)
    
    for cmd in commands:
        # 현재 위치가 오프닝 구간이면
        if op_start <= curr_pos <= op_end:
            curr_pos = op_end # 오프닝 끝 시점으로 이동한다
            
        if cmd == "prev": 
            curr_pos = max(0, curr_pos - 10) # 10초 이전으로 이동하되, 0보다는 작지 않아야 한다
        elif cmd == "next":
            curr_pos = min(video_len, curr_pos + 10) # 10초 후로 이동하되, 비디오의 길이보다는 크지 않아야 한다
            
        # 바뀐 시기가 오프닝 구간이면
        if op_start <= curr_pos <= op_end:
            curr_pos = op_end # 오프닝 끝 시점으로 이동한다
    
    return seconds_to_time(curr_pos)