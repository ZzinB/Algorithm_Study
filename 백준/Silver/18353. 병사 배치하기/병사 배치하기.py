def main():
    N = int(input())
    soldiers = list(map(int, input().split()))
    dp = [1] * N

    for i in range(N):
        for j in range(i):
            if soldiers[j] > soldiers[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(N - max(dp))

if __name__ == "__main__":
    main()