def solution(spell, dic):
    answer = 0
    for d in dic:
        if sorted(d) == sorted(spell):
            return 1
    return 2