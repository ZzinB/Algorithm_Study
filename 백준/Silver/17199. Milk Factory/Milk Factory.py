import sys
input= sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())
graph = [[] for _ in range(N+1)]


for _ in range(N-1):
  a,b = map(int,input().split())
  graph[b].append(a) #그래프 요소 추가

def dfs(v):
  visited[v] = True
  for i in graph[v]:
    if not visited[i]:
      dfs(i)
      visited[i] = True

for i in range(1,N+1):
  visited = [False] * (N+1) #매번 visited 를 초기화하면서 
  if not visited[i]: 
    dfs(i)
  if visited.count(True)==N: #i에서 시작한 dfs가 모든 그래프를 돌 수 있으면
    print(i) #i를 출력하고 종료
    exit()

print(-1) #만족하는 i가 없으면 -1을 출력