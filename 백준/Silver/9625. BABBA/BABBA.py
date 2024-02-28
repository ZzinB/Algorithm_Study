K = int(input())

fib = [0] * (K + 1)
fib[1] = 1

for i in range(2, K + 1):
    fib[i] = fib[i - 1] + fib[i - 2]

A_count = fib[K - 1]
B_count = fib[K]

print(A_count, B_count)
