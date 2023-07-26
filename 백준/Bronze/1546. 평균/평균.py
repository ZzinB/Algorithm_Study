N = int(input())
score = list(map(int, input().split()))
M = max(score)
sum = 0

for i in range(N):
    score[i] = score[i]/M*100
    sum += score[i]

avg = sum/N
print(avg)