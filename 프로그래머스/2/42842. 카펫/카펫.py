def solution(brown, yellow):
    size = brown + yellow
    # 약수의 쌍을 찾아가며 가로, 세로 길이 검증
    # total의 제곱근까지만 반복 
    for i in range(1, int(size**0.5)+1):
        #n을 i로 나누었을 때 나누어 떨어지면 그게 일부의 약수들 
        if size % i == 0:
            # i가 가로 길이, total//i가 세로 길이
            y = (i-2) * (size//i-2)
            # 노란색수가 일치하는지 확인
            if y == yellow:
                return [size//i, i]



