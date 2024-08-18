def backtrack(start, current):
    # 수열의 길이가 M에 도달하면 출력
    if len(current) == M:
        print(' '.join(map(str, current)))
        return
    
    for i in range(start, N + 1):
        # 현재 수열에 숫자를 추가, 재귀 호출
        backtrack(i + 1, current + [i])

N, M = map(int, input().split())

backtrack(1, [])
