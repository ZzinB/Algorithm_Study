def solution(id_pw, db):
    answer = 'fail'
    Id, pw = id_pw
    for data in db:
        loginId, loginpw = data
        if loginId == Id:
            if loginpw == pw:
                answer = "login"
            elif loginpw != pw:
                answer = "wrong pw"
            break
    return answer