def solution(sizes):
    w = []
    h = []
    for s in sizes:
        w.append(max(s))
        h.append(min(s))
    return max(w) * max(h)