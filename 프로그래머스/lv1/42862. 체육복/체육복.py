def solution(n, lost, reserve):
    only_reserve = set(reserve) - set(lost) 
    only_lost = set(lost) - set(reserve)

    for i in only_reserve :
        if i-1 in only_lost :
            only_lost.remove(i-1)
        elif i+1 in only_lost :
            only_lost.remove(i+1)

    return n - len(only_lost)