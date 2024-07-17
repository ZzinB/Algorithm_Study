from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 이동방향
d = [(-1, 0), (1, 0), (0, -1), (0, 1), 
     (-1, -1), (1, -1), (-1, 1), (1, 1)]
q = deque()

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            # 맵에서 벗어나는 경우
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            # 상어가 없는 지점 or 미탐색 지점인지 확인
            if not graph[nx][ny]:
                # 새로운 지점의 거리 정보 업데이트
                graph[nx][ny] = graph[x][y] + 1
                # 새로운 지점의 좌표를 큐에 삽입
                q.append((nx, ny))

# 상어의 위치에서부터 탐색 시작
for i in range(n):
    for j in range(m):
        # 상어 위치일 경우
        if graph[i][j]:
            # 상어 위치를 큐에 삽입
            q.append((i, j))

bfs()

print(max(map(max, graph))-1)