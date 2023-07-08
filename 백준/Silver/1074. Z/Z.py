import sys


def visited(n, r, c):
    global res

    if r == R and c == C:
        print(int(res))
        exit(0)

    if not (r <= R < r + n and c <= C < c + n):
        res += n * n
        return

    visited(n/2, r, c) # 1사분면
    visited(n/2, r, c + n/2) # 2사분면
    visited(n/2, r + n/2, c) # 3사분면
    visited(n/2, r + n/2, c + n/2) # 4사분면


N, R, C = map(int, sys.stdin.readline().split())
res = 0

visited(2 ** N, 0, 0)