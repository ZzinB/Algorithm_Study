def solution(babbling):
    answer = 0
    can = ['aya', 'ye', 'woo', 'ma']
    for ba in babbling:  
        for c in can:
            if c * 2 not in ba: 
                ba = ba.replace(c, ' ')
        if ba.isspace(): 
            answer += 1
    return answer