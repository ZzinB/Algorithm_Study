P = int(input())
for _ in range(P):
    heights = list(map(int,input().split()))  # 키 정보 입력, heights[0]은 테스트 케이스 번호
    answer = 0  # 각 테스트 케이스에서의 물러난 수
    # 버블소트: 키 순서대로 정렬
    for i in range(1, len(heights)-1):
        for j in range(i+1, len(heights)): # i 뒤에 애들과 전부 비교
            if heights[i] > heights[j]:  # i가 더 크면
                heights[i], heights[j] = heights[j], heights[i]  # 자리 바꾸기
                answer += 1 # 물러난 수 증가
    print(heights[0], answer)