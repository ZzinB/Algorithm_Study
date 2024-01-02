import sys

N, M = map(int, input().split())
memo = {}
answer = N

for _ in range(N):
    memo[sys.stdin.readline().rstrip()] = 1

for _ in range(M):
    post = sys.stdin.readline().rstrip().split(',')
    for keyword in post:
        if keyword in memo and memo[keyword] == 1:
            memo[keyword] = 0
            answer -= 1
    print(answer)