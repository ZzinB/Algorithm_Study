import sys

N, M = map(int, input().split())
notes = set(sys.stdin.readline().strip() for _ in range(N))
keywords = set(notes)


for i in range(N+2, N+M+2):
    post = set(sys.stdin.readline().strip().split(","))
    keywords -= post

    print(len(keywords))