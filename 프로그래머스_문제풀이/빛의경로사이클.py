# 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def solution(grid):
    answer = []
    board = [[[True] * 4 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    
    for nx in range(len(grid)):
        for ny in range(len(grid[0])):
            for nd in range(4):
                if not board[nx][ny][nd]:
                    continue
                
                count = 0
                x, y, d = nx, ny, nd
                while 1:
                    count += 1
                    board[x][y][d] = False
                    
                    if grid[x][y] == 'L':
                        d = (d - 1) % 4
                    elif grid[x][y] == 'R':
                        d = (d + 1) % 4
                        
                    x = (x + dx[d]) % len(grid)
                    y = (y + dy[d]) % len(grid[0])
                    
                    if x == nx and y == ny and d == nd:
                        break
                answer.append(count)
                
    return sorted(answer)