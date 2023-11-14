from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append((0, 0))
    while queue:
        idx, tmp = queue.popleft()
        if idx == len(numbers):
            if tmp == target:
                answer +=1
        else:
            queue.append((idx+1, tmp+numbers[idx]))
            queue.append((idx+1, tmp-numbers[idx]))
    return answer
