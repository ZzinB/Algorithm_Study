def solution(my_string, m, c):
    li = [my_string[i:i+m] for i in range(0, len(my_string), m)]
    answer = "".join([li[i][c-1] for i in range(0, len(li))])
    return answer