def solution(ineq, eq, n, m):
    if ineq == ">" and eq == "=":
        return int(n >= m)
    elif ineq == "<" and eq == "=":
        return int(n <= m)
    elif ineq == ">" and eq == "!":
        return int(n > m)
    elif ineq == "<" and eq == "!":
        return int(n < m)
    else:
        return 0