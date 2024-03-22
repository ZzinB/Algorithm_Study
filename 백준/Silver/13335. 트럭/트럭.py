import sys

n, w, l = map(int, input().split())  # 트럭의 수, 다리의 길이, 최대하중
q = list(map(int, input().split()))  # 각 트럭의 무게

b = [0] * w  # 다리 
time = 0  

# 다리가 비어있을 때까지 반복
while b:
    time += 1 
    b.pop(0)  # 다리 첫번째 요소 pop하여 트럭 이동

    # 트럭이 아직 남아있을 때
    if q:
        # 다리에 새로운 트럭이 올라갈 수 있는지 확인
        if sum(b) + q[0] <= l:  # 다리 위의 트럭 무게와 새 트럭의 무게 합이 최대하중 이하인지 확인
            b.append(q.pop(0))  # 다리에 새로운 트럭 추가
        else:
            b.append(0)  # 다리에 새로운 트럭을 추가하지 않고, 무게가 0인 트럭을 추가하여 위치를 이동

print(time)  
