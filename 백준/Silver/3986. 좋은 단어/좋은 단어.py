def solution(n, words):
    cnt = 0
    
    for word in words:
        stack = []
        for char in word:
            if stack and stack[-1] == char:
                stack.pop()  # 짝이 맞으면 스택에서 제거
            else:
                stack.append(char)  # 스택에 추가
        
        if not stack:  # 스택이 비어있다면 '좋은 단어'
            cnt += 1
    
    return cnt

N = int(input())
words = [input().strip() for _ in range(N)]

print(solution(N, words))
