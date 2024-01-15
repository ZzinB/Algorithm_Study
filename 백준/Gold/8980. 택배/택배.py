# input 1 : 마을 수 N과 트럭의 용량 C
N, C = map(int, input().split())
# input 2 : 보내는 박스 정보의 개수 M
M = int(input())
# input 3 : 다음 M개의 박스 정보 -  박스를 보내는 마을번호(s), 박스를 받는 마을번호(r), 보내는 박스 개수(b)
boxes = [list(map(int, input().split())) for _ in range(M)]
# 도착지가 가까운 순으로 정렬 : 가까운 순으로 빠르게 운송하여 최대한 많이 운송!
boxes.sort(key=lambda x :  x[1])
# 지역마다 전달할 최대 박스 개수 (C개)
max_box = [C] * (N+1)
# output : 트럭 한 대로 배송할 수 있는 최대 박스 수
answer = 0

for s, r, b in boxes:
    _min = C
    # 출발지에서 도착지까지
    for i in range(s, r):
        # 옮길 수 있는 박스 개수(_min)와 지역 운송 최대 박스 개수(max_box) 중 작은 값
        _min = min(_min, max_box[i])
    # 옮길 수 있는 박스 개수(_min)와 실제 박스 개수(b) 중 작은 값
    _min = min(_min, b)
    for i in range(s, r):
        # 옮긴 만큼은 빼기 !
        max_box[i] -= _min
    # 뺐던 박스 개수
    answer += _min
print(answer)