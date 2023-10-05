def solution(quiz):
    answer = []
    for q in quiz:
        if eval(q.split('=')[0]) == int(q.split('=')[1]):
            answer.append('O')
        else:
            answer.append('X')
    return answer