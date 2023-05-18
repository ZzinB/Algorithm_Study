import sys
n, point, p = map(int, sys.stdin.readline().split())
if n:
    m = sorted(list(map(int, sys.stdin.readline().split())) + [point], reverse=True)
    answer = m.index(point) + 1  

    if answer > p:
        print(-1)
    else:
        if n == p and point == m[-1]:
            print(-1)
        else:
            print(answer)
else:
    print(1)