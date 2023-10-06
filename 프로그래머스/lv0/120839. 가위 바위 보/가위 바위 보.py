def solution(rsp):
    win = {'0':'5', '2':'0', '5':'2'}
    answer = ''.join(win[i] for i in rsp)
    return answer