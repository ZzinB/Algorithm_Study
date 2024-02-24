n, m = map(int, input().split())
male = list(map(int, input().split()))
female = list(map(int, input().split()))

male.sort()
female.sort()

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

# 성격 차이의 합을 계산
for i in range(1, n+1):
    for j in range(1, m+1):
        # d[i][j]: 첫 번째 남자 i명과 첫 번째 여자 j명을 매칭했을 때의 최소 성격 차이의 합
        # 현재 남자와 여자의 성격 차이를 더해줌
        dp[i][j] = dp[i-1][j-1] + abs(male[i-1] - female[j-1])
        # 여자가 더 적은 상황
        if i > j:
            dp[i][j] = min(dp[i][j], dp[i-1][j])
        # 남자가 더 적은 상황
        elif i < j:
            dp[i][j] = min(dp[i][j], dp[i][j-1])

print(dp[n][m])
