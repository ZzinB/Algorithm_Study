def solution(arr):
    X = []  
    for a in arr:
        X.extend([a] * a)  
    return X

