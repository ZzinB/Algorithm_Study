import sys
input = sys.stdin.readline

n = int(input())
ans = [-1 for _ in range(n)]
A = list(map(int, input().split()))
mystack = []

for i in range(n):
    while mystack and A[mystack[-1]] < A[i]: #오큰수 조건
        ans[mystack.pop()] = A[i] #정답 리스크에 오큰수 저장
    mystack.append(i)
print(*ans)