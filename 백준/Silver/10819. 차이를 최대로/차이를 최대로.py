N = int(input())
A = list(map(int, input().split()))

# 순열을 저장할 리스트
permutations = []

# 순열을 생성
def generate_permutations(current, remaining):
    # 모든 숫자를 다 사용했다면
    if not remaining:
        # 완성된 순열을 permutations에 추가
        permutations.append(current)
        return
    # 순열을 생성하면서 (remaining -> current)
    for i in range(len(remaining)):
        # current에 추가할 때(remaining[i]), 해당 숫자 제외하고 새로운 remaining으로 다시 순열 생성
        generate_permutations(current + [remaining[i]], remaining[:i] + remaining[i+1:])

generate_permutations([], A)

# 최댓값 찾기
max_value = 0

# 생성된 모든 순열에 대해
for perm in permutations:
    total = 0
    # 각 순열의 인접한 두 원소 절대값 차이를 더함
    for i in range(N - 1):
        total += abs(perm[i] - perm[i + 1])
    # 현재 순열이 지금까지의 최대값보다 크면 update
    if total > max_value:
        max_value = total

print(max_value)
