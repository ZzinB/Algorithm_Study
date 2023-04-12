import sys
from collections import deque
input = sys.stdin.readline

N, L = map(int, input().split())
mydeque = deque()
now = list(map(int, input().split()))

for i in range(N):# now list 탐색 
    while mydeque and mydeque[-1][0] > now[i]:# deque 마지막 위치에서부터 현재 값보다 큰 값은 제거
        mydeque.pop()
    mydeque.append((now[i], i))# deque 마지막 위치에 현재 값 저장
    if mydeque[0][1] <= i - L:# deque 1번째 위치에서부터 size(L)의 범위를 벗어난 값을 제거
        mydeque.popleft()        
    print(mydeque[0][0], end=' ')# deque 1번째 데이터 출력