import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M, K = map(int, input().split())

graph = [list(input().rstrip()) for _ in range(N)]

def DFS(x, y, count):
    if count == K and x == 0 and y == M - 1:
        return 1
    paths = 0
    for nx, ny in zip([x-1, x+1, x, x], [y, y, y-1, y+1]):
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == '.':
            graph[nx][ny] = 'T'
            paths += DFS(nx, ny, count + 1)
            graph[nx][ny] = '.'
    return paths

graph[N-1][0] = 'T'
answer = DFS(N-1, 0, 1)
print(answer)
