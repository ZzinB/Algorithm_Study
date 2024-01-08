# 1. 입력받기 (N)
N = int(input())
# 2. 상근, 창영 번갈아가면서 1개, 또는 3개 가져가기
# 2-1. 상근이가 먼저 시작
# 3. 마지막 돌을 가져가는 사람이 승리
# 4. 완벽한 게임 후 승자 출력

# N = 1, sk -> sk
# N = 2, sk1 cy1 -> cy
# N = 3, sk3 -> sk
# N = 4, sk3 cy1 -> cy
# N = 5, sk3 cy1 sy1 -> sk


if N % 2 == 0:
    print('CY')
else:
    print('SK')