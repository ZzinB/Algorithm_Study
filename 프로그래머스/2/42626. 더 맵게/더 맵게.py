import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1  # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우
        # 가장 맵지 않은 두 음식을 꺼내서 섞음
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        mixed = first + (second * 2)
        # 섞은 음식의 스코빌 지수를 힙에 추가
        heapq.heappush(scoville, mixed)
        cnt += 1
    return cnt