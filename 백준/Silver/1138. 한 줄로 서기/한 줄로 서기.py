N = int(input())
people = list(map(int, input().split()))
answer = [0] * N

for idx, person in enumerate(people):
    cnt = 0
    for j in range(N):
        if cnt == person and answer[j] == 0:
            answer[j] = idx+1
            break
        elif answer[j] == 0:
            cnt += 1

print(*answer)