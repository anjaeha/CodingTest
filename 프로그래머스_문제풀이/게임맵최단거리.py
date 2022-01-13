from collections import deque

dx = [-1, 1, 0, 0]
dy = [0 ,0, -1, 1]

def solution(maps):
    q = deque([(0, 0)])
    
    board = [[-1] * len(maps[0]) for _ in range(len(maps))]
    board[0][0] = 1
    while q:
        x, y = q.popleft()
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                if board[nx][ny] == -1 and maps[nx][ny] == 1:
                    q.append((nx, ny))
                    board[nx][ny] = board[x][y] + 1
                    
    return board[-1][-1]