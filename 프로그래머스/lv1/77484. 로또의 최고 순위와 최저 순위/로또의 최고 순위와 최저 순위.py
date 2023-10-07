def solution(lottos, win_nums):
    rank=[6, 6, 5, 4, 3, 2, 1]
    zero = lottos.count(0)
    answer = 0
    for win in win_nums:
        if win in lottos:
            answer += 1
    return rank[zero + answer], rank[answer]