def solution(m, n, puddles):
    dp = [[0] * (m+1) for i in range(n+1)] #dp 초기화
    dp[1][1] = 1  #시작위치(집)
    
    #웅덩이 위치라면? dp = -1 로 
    for i, j in puddles:
        dp[j][i] = -1
    
    # 경로찾기
    for i in range(1, n+1):
        for j in range(1, m+1):
            #웅덩이(dp = -1)라면? continue 
            if dp[i][j] == -1:
                dp[i][j] = 0
                continue
            #웅덩이가 아니라면? 현재 칸 = 왼쪽 칸 + 윗 칸
            dp[i][j] += (dp[i-1][j] + dp[i][j-1]) % 1000000007
    return dp[n][m]