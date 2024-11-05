def solution(rsp):    
    rsp_dict = {'0': '5', '2': '0', '5':'2'}
    return ''.join(rsp_dict[i] for i in rsp)