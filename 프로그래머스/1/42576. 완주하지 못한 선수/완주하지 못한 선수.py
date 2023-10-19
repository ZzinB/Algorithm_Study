def solution(participant, completion):
    hash_dict = {}
    for p in participant:
        hash_dict[p] = hash_dict.get(p, 0) + 1
    for c in completion:
        hash_dict[c] -= 1
    for p in participant:
        if hash_dict[p] == 1:    return p