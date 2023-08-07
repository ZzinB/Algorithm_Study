def solution(str1, str2):
    list = []
    for i in range(len(str1)):
        list.append(str1[i] + str2[i])
    return ''.join(list)