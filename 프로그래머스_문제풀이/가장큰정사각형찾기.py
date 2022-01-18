def solution(board):
    answer = 0
    
    for x in range(1, len(board)):
        for y in range(1, len(board[0])):
            if board[x][y] >= 1:
                board[x][y] += min(board[x - 1][y - 1], board[x - 1][y], board[x][y - 1])
    
    for i in board:
        answer = max(answer, max(i))
    
    return answer ** 2