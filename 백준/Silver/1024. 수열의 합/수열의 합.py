N, L = map(int, input().split())
x = []

def get_arr(length, N):
    x = N - (length * (length+1) // 2)
    return x / length

for i in range(L, 101):

    a = get_arr(i, N)
    if int(a) == a :
        a = int(a)
        sub_sum = sum(range(a+i+1)) - sum(range(a+1))
        if sub_sum == N :
            x = (list(range(a + 1, a + i + 1)))
            x = list(map(str, x))
            break

print(' '.join(x) if x != [] and len(x) <= 100 else -1)