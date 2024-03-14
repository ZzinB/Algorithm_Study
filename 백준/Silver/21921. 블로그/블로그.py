N, X = map(int, input().split())
visit = list(map(int, input().split()))

if(max(visit)) == 0:
    print("SAD")

else:
    total = sum(visit[:X])
    max_total = total
    cnt = 1

    for i in range(X, N):
        total += visit[i]
        total -= visit[i-X]

        if(total > max_total):
            max_total = total
            cnt = 1
        elif (total == max_total):
            cnt += 1

    print(max_total)
    print(cnt)