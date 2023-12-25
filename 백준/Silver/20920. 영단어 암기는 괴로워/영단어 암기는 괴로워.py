import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())  # 단어 개수, 단어 길이
words = {}  

for _ in range(N):
    word = input().rstrip()

    if len(word) < M:  # 단어가 M 미만인 경우 패스
        continue
    else:  # 단어가 M 이상인 경우
        if word in words:  # 단어가 존재한다면
            words[word] += 1
        else:  # 단어가 없는 경우
            words[word] = 1

sorted_words = sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for word, count in sorted_words:
    print(word)
