def evaluate(pw):
    vowels = set('aeiou') # 모음

    # 규칙 1 : 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
    if not any(v in vowels for v in pw):
        return "not acceptable"

    # 규칙 2 : 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
    # v_cnt: 현재까지 나온 연속된 모음의 개수
    # c_cnt: 현재까지 나온 연속된 자음의 개수
    v_cnt = c_cnt = 0
    for char in pw:
        # 현재 문자가 모음인 경우
        if char in vowels:
            v_cnt += 1
            c_cnt = 0
        else:
            c_cnt += 1
            v_cnt = 0

        # 모음이나 자음이 3개 연속으로 나오면
        if v_cnt == 3 or c_cnt == 3:
            return "not acceptable"

    # 규칙 3 : 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
    for i in range(1, len(pw)):
        # 현재 글자와 바로 이전 글자가 같고 and 'e'나 'o'가 아닌 경우
        if pw[i] == pw[i - 1] and pw[i] not in {'e', 'o'}:
            return "not acceptable"

    # 모든 규칙 통과
    return "acceptable"


while True:
    pw = input().strip()
    if pw == "end":
        break

    result = evaluate(pw)
    print(f"<{pw}> is {result}.")

