def solution(A, B):
    answer = -1
    if A == B:
        return 0
    for i in range(1, len(A)):
        A = A[-1] + A[0:-1]
        if A == B:
            return i  
    return answer