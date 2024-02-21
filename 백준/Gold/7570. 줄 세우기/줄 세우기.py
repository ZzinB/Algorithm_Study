N = int(input())
childrens = list(map(int, input().split()))
childrens.insert(0, 0)

result = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    result[childrens[i]] = i

cnt = 1
max_length = -1

for i in range(1, N):
    if result[i] < result[i + 1]:
        cnt += 1

        if cnt > max_length:
            max_length = cnt

    else:
        cnt = 1
print(N - max_length if max_length != -1 else 0)