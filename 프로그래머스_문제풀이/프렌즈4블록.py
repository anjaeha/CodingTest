from collections import deque
def solution(m, n, board):
    answer = 0
    board = [list(board[i]) for i in range(m)]
    flag = True
    while flag:
        flag = False
        graph = [[False] * n for _ in range(m)]
        for x in range(m - 1):
            for y in range(n - 1):
                if board[x][y] != -1:
                    now = board[x][y]
                    if now == board[x + 1][y] and now == board[x][y + 1] and now == board[x + 1][y + 1]:
                        graph[x][y], graph[x + 1][y], graph[x][y + 1], graph[x + 1][y + 1] = True, True, True, True

        for x in range(m):
            for y in range(n):
                if graph[x][y]:
                    board[x][y] = -1
                    answer += 1
                    flag = True
        
        
        for y in range(n):
            bag = deque()
            for x in range(m - 1, -1, -1):
                if board[x][y] != -1:
                    bag.append(board[x][y])
                    board[x][y] = -1
        
            for x in range(m - 1, -1, -1):
                if bag:
                    board[x][y] = bag.popleft()
                    
    
    return answer