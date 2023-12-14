import heapq
import sys

def main():
    n = int(input())
    heap = []

    for _ in range(n):
        x = int(sys.stdin.readline().rstrip())

        if x == 0:
            # 배열에서 가장 작은 값 출력 및 제거
            if not heap:
                print(0)
            else:
                print(heapq.heappop(heap))
        else:
            # 배열에 자연수 x 추가
            heapq.heappush(heap, x)

if __name__ == "__main__":
    main()
