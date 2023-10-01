def solution(a, b, n):
    answer = 0
    while n >= a:
        cnt = n // a * b
        coke = n % a        
        answer += cnt
        n = coke + cnt
    return answer