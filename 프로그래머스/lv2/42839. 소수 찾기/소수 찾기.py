from itertools import permutations

def is_prime_number(x) :
    if x < 2 : 
        return False
    for i in range(2, x) :
        if x % i == 0 :
            return False  
    return True

def solution(numbers):
    answer = 0
    li = []
    for i in range(1, len(numbers)+1):
        li.append(list(set(map(''.join, permutations(numbers, i)))))
        per = list(set(map(int, set(sum(li, [])))))
    for p in per :
        if is_prime_number(p) == True :
            answer += 1

    return answer