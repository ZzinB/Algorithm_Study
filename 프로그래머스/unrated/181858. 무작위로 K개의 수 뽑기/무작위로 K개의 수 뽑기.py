def solution(arr, k):
    answer = []
    unique = set()
    for num in arr:
        if num not in unique:
            answer.append(num)
            unique.add(num)
        if len(answer) == k:
            break
    while len(answer) < k:
        answer.append(-1)
    return answer