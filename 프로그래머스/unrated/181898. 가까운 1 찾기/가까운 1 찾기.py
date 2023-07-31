def solution(arr, idx):
    answer = -1
    for i, num in enumerate(arr):
        if idx <= i and num == 1:
            return i
    return answer