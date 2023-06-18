def solution(clothes):
    hash = {}
    
    for clothe, type in clothes:
        hash[type] = hash.get(type, 0) + 1
    answer = 1
    
    for type in hash:   
        answer *= (hash[type] + 1)
    
    return answer - 1