def solution(phone_number):
    hide = len(phone_number)-4
    answer = '*' * hide + phone_number[-4:]
    return answer