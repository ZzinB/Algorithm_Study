def solution(keyinput, board):
    start = [0,0]
    move = {'up' : [0,1], 'down' : [0,-1],'left' : [-1,0], 'right' : [1,0]}
    for i in keyinput:
        dx, dy = move[i]
        if abs(start[0] + dx)> board[0]//2 or abs(start[1]+dy) >board[1]//2:
            continue
        else:
            start[0] += dx
            start[1] += dy
    return start