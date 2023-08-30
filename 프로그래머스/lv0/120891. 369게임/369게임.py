def solution(order):
    return len([num for num in list(str(order)) if int(num) in {3, 6, 9}])