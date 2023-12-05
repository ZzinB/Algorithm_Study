def solution(array, n):
    array.sort()
    answer = array[0]
    tmp = abs(n - answer)
    for num in array:
        x = abs(n - num)
        if x < tmp:
            tmp = x
            answer = num
    return answer