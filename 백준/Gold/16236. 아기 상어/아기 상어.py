from collections import deque
import sys
input = sys.stdin.readline

def find_shark():
    for i in range(n):
        for j in range(n):
            if board[i][j] == 9:
                board[i][j] = 0
                return i,j
            
def bfs(x,y):
    cand = []
    visited = [[False]*n for _ in range(n)]
    visited[x][y] = True
    q = deque([(0,x,y)])
    min_w = float('inf')
    
    while q:
        w,cx,cy = q.popleft()
        for a,b in move:
            dx,dy = cx+a, cy+b
            if dx>=n or dx<0 or dy>=n or dy<0: # 범위 벗어나는 경우
                continue
            if visited[dx][dy] or board[dx][dy] > size: # 이미 방문했거나 큰 물고기인 경우
                continue
        
            visited[dx][dy] = True
            dw = w+1
            
            if 0 < board[dx][dy] < size: 
                if min_w == float('inf'): 
                    min_w = dw
                elif dw > min_w:
                    return cand
                cand.append((dw,dx,dy))
                
            q.append((dw,dx,dy))
            
    return cand

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
move = [(0,1),(1,0),(0,-1),(-1,0)]
size, ate = 2,0
x,y = find_shark()
ans = 0

while True:
    cand = bfs(x,y)
    if not cand:
        break
    
    cand.sort()
    w,x,y = cand[0]
    ans += w
    board[x][y] = 0
    
    ate += 1
    if size == ate:
        size += 1
        ate = 0
        
print(ans)