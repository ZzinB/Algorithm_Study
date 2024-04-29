from itertools import product

def solution(word):
    words = []
    vowel = ['A', 'E', 'I', 'O', 'U'] # 모음
    for i in range(1, 6):
        #모든 조합 이용
        for j in product(vowel, repeat=i):
            words.append(''.join(j))
    words.sort()
    return words.index(word)+1