n = int(input())
arr = []
for _ in range(n): 
    arr.append(int(input()))
dp = [1] * (n+1)
len = 0

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            if dp[i] < dp[j]+1: 
                dp[i] = dp[j]+1

    if len < dp[i]:
        len = dp[i]

print(n - len)