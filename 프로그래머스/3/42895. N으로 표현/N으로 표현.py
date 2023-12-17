def solution(N, number):
    # DP 배열 초기화
    dp = [set() for _ in range(9)]

    # 모든 경우의 수 저장
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))

    # dp
    for i in range(1, 9):
        for j in range(1, i):
            for x in dp[j]:
                for y in dp[i - j]:
                    dp[i].add(x + y)
                    dp[i].add(x - y)
                    dp[i].add(x * y)
                    if y != 0:
                        dp[i].add(x // y)

        # 목표 숫자에 도달하면 결과 반환
        if number in dp[i]:
            return i
    return -1