import sys
N = int(input())
ranks = [int(sys.stdin.readline()) for _ in range(N)]

#예상등수 정렬
ranks.sort() 

result = 0
for i in range(N):
    # 예상 등수와 실제 등수 사이의 차이 (=불만도 최소)를 결과에 더함
    result += abs(ranks[i] - (i + 1)) 

print(result)
