import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [[0] * (n+1)]
D = [[0] * (n+1) for _ in range(n+1)]

for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

for i in range(n+1):
    D[i][1] = D[i-1][1] + A[i][1]
    D[1][i] = D[1][i-1] + A[1][i]
    
for i in range(2, n+1):
    for j in range(2, n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j] #합을 구하고 겹치는 부분은 빼주기

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2]  - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)