import sys
N = sys.stdin.readline().strip()
num = 0
while len(N):
    num += 1
    numbers = str(num)
    while len(numbers) and len(N):
        if numbers[0] == N[0]:
            N = N[1:]
        numbers = numbers[1:]
print(num)