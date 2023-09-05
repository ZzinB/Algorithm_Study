def solution(picture, k):
    answer = []
    for row in picture: 
        re = ''
        for pixel in row:
            re += pixel * k 
        for _ in range(k):
            answer.append(re) 
    return answer