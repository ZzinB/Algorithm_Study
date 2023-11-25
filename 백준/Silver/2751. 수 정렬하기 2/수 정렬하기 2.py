import sys
n = int(input())
numbers = [int(sys.stdin.readline()) for _ in range(n)]

sorted_numbers = sorted(numbers)
for num in sorted_numbers:
    print(num)
