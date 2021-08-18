import sys
input = sys.stdin.readline

game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
table_shape = []
board_shape = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = []


def table_dfs(x, y):
    global startx, starty

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= len(table) or ny >= len(table):
            continue

        if table[nx][ny] == 1:
            table[nx][ny] = 0
            temp.append((nx - startx, ny - starty))
            table_dfs(nx, ny)

def board_dfs(x, y):
    global startx, starty

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= len(game_board) or ny >= len(game_board):
            continue

        if game_board[nx][ny] == 0:
            game_board[nx][ny] = 1
            temp.append((nx - startx, ny - starty))
            board_dfs(nx, ny)
            

for i in range(len(table)):
    for j in range(len(table)):
        if table[i][j] == 1:
            table[i][j] = 0
            startx, starty = i, j
            temp = [(i - startx, j - starty)]
            table_dfs(i, j)
            table_shape.append(temp)
        if game_board[i][j] == 0:
            game_board[i][j] = 2
            startx, starty = i, j
            temp = [(i - startx, j - starty)]
            board_dfs(i, j)
            board_shape.append(temp)


for i in board_shape:
    if i in table_shape:
        board_shape.remove(i)
        table_shape.remove(i)
        result.append(i)

print(board_shape)
print(table_shape)