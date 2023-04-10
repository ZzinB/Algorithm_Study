def solution(my_string):
    answer = ''
    new_list = sorted(my_string.lower())        

    for v in range(len(new_list)):
        answer += new_list[v]

    return answer