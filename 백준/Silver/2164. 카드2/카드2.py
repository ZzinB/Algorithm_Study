from collections import deque

def solution(N):
    cards = deque(range(1, N + 1))

    while len(cards) > 1:
        # 제일 위에 있는 카드를 버린다.
        cards.popleft()
        # 그 다음 제일 위에 있는 카드를 제일 아래로 옮긴다.
        cards.append(cards.popleft())
    return cards[0]

def main():
    N = int(input())
    result = solution(N)
    print(result)

if __name__ == "__main__":
    main()
