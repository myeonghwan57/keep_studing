def solution(board):
    #X의 개수가 많은면 안된다.
    O_cnt = 0
    X_cnt = 0
    O_win = 0
    X_win = 0
    for i in board:
        O_cnt += i.count('O')
        X_cnt += i.count('X')

    if O_cnt + X_cnt == 0:
        return 1
    if O_cnt > X_cnt + 1:
        return 0
    if O_cnt < X_cnt:
        return 0

    for i in range(3):
        # 세로 이기는 경우 O, X
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            if board[1][i] == 'O':
                O_win += 1
            elif board[1][i] == 'X':
                X_win += 1
        # 가로 이기는 경우 O, X
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            if board[i][1] == 'O':
                O_win += 1
            elif board[i][1] == 'X':
                X_win += 1
        # 양대각선으로 이기는 경우 
        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            if board[1][1] == 'O':
                O_win += 1
            elif board[1][1] == 'X':
                X_win += 1
    if X_win == O_win and O_win == 0:
        return 1
    if X_win == 0 and O_win > 0:
        if X_cnt < O_cnt:
            return 1
    if X_win > 0 and O_win == 0:
        if X_cnt == O_cnt:
            return 1
    return 0 

    
