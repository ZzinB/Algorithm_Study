#1. 근손실로 인한 중량이 500보다 작아지지 않게 하도록 경우의 수를 탐색
#2. 매일같이 근손실이 일어나므로 K를 빼야함, 중복체크(키트사용)
#3. 백트래킹 : 다음 kit로 이동하여 재귀

# 현재 근육량 + 현재 운동 키트 중량 - K >= 0 일 때 재귀
def backtracking(w, cnt):
    global result
    # 1일에 1 kit 사용 : cnt = N 이면 result += 1
    if cnt == N:
        result += 1
        return

    # w가 500보다 작아지지 않도록 : 무게가 500보다 작으면 종료
    if w < 500:
        return

    # 매일 근손실 (중량 -K)
    w -= K

    # N일까지 N개 운동 키트
    for i in range(N):
        #사용하지 않은 kit
        if not used[i]:
            used[i] = True
            backtracking(w+kit[i], cnt+1)
            used[i] = False

# INPUT 1: N K
# INPUT 2: 운동 키트의 중량 증가량 A
N, K = map(int, input().split())
kit = list(map(int, input().split()))
used = [False] * N
result = 0
backtracking(500, 0)
# OUTPUT : 500 이상이 되도록 하는 경우의 수
print(result)