def solution(array):
    result = ""
    for num in array:
        result += str(num)
    return result.count("7")