import sys

input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * n
C = [0] * m
answer = 0

S[0] = A[0]   # 합배열의 첫번째는 입력값의 첫번째로 지정
for i in range(1, n):
    S[i] = S[i-1] + A[i]   # 합 배열에 담기

for i in range(n):
    reminder = S[i] % m    # m으로 나누고 나머지 없으면 나눠지는거
    if reminder == 0 :
        answer += 1
    C[reminder] += 1

for i in range(m):
    if C[i] > 1:
        answer += (C[i] * (C[i]-1) // 2)   #combination

print(answer)