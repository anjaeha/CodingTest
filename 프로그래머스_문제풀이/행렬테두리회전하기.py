def solution(rows, columns, queries):
    board = [[(j * columns) + i for i in range(1, columns + 1)] for j in range(rows)]
    answer = []
    for query in queries:
        MIN = 999999
        temp = board[query[0] - 1][query[1] - 1]
        for i in range(query[0] - 1, query[2] - 1):
            board[i][query[1] - 1] = board[i + 1][query[1] - 1]
            MIN = min(MIN, board[i + 1][query[1] - 1])
        
        for i in range(query[1] - 1, query[3] - 1):
            board[query[2] - 1][i] = board[query[2] - 1][i + 1]
            MIN = min(MIN, board[query[2] - 1][i + 1])
            
        for i in range(query[2] - 1, query[0] - 1, -1):
            board[i][query[3] - 1] = board[i - 1][query[3] - 1]
            MIN = min(MIN, board[i - 1][query[3] - 1])
            
        for i in range(query[3] - 1, query[1] - 1, -1):
            board[query[0] - 1][i] = board[query[0] - 1][i - 1]
            MIN = min(MIN, board[query[0] - 1][i - 1])
            
        board[query[0] - 1][query[1]] = temp
        MIN = min(MIN, temp)
        
        answer.append(MIN)
        
    return answer