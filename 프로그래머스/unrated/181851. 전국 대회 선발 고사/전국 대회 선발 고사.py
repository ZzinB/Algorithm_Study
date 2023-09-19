def solution(rank, attendance):
    n = len(rank)
    answer =0
    li = []

    for i in range(n):
        if attendance[i]:
            li.append([rank[i], i])

    li.sort(key = lambda v : v[0])

    return 10000 * li[0][1] + 100 * li[1][1] + li[2][1]