def solution(m, n, b):
    answer = 0
    
    board = []
    for i in range(m):
        board.append(list(b[i]))
        
    while 1:
        check = []
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == '0':
                    continue
                if board[i][j] == board[i+1][j]:
                    if board[i][j] == board[i][j+1] == board[i+1][j+1]:
                        check.append((i, j))
                        check.append((i+1, j))
                        check.append((i, j+1))
                        check.append((i+1, j+1))
        if len(check) == 0:
            break
        else:
            answer += len(set(check))
            for c in check:
                board[c[0]][c[1]] = '0'
            
            for c in check:
                up = c[0] - 1
                down = c[0]
                
                while up >= 0:
                    if board[down][c[1]] == '0' and board[up][c[1]] != '0':
                        board[down][c[1]] = board[up][c[1]]
                        board[up][c[1]] = '0'
                        down -= 1
                    up -= 1
                    
    return answer