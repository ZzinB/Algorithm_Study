import sys
N = int(input())

num_arr = [int(x) for x in input().split()]

M = int(input())

dp = [[0] * (N) for _ in range(N)]

for i in range(N):
    dp[i][i] = 1

for i in range(N - 1): 
    if num_arr[i] == num_arr[i + 1]:
        dp[i][i + 1] = 1

for num_len in range(2, N):
    for start in range(N - num_len):
        end = start + num_len
        if num_arr[start] == num_arr[end]:
            if dp[start + 1][end - 1] == 1:
                dp[start][end] = 1

for _ in range(M):
    S, E = map(int, sys.stdin.readline().split())
    print(dp[S - 1][E - 1])