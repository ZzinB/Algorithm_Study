def solution(document, word):
    count = 0
    index = 0
    
    while index <= len(document) - len(word):
        # 현재 위치에서 단어가 발견되면
        if document[index:index + len(word)] == word:
            count += 1
            index += len(word)  # 단어의 길이만큼 이동하여 중복 카운팅 방지
        else:
            index += 1  # 한 칸 이동하여 다음 위치에서 검색
    
    return count

document = input().strip()
word = input().strip()

print(solution(document, word))
