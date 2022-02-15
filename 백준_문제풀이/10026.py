import sys
sys.setrecursionlimit(10 ** 4)
n = int(input())
graph = [list(input()) for _ in range(n)]
board = [i[:] for i in graph]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, game):
    game[x][y] = '.'
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < n:
            if game[nx][ny] == now:
                dfs(nx, ny, game)

for i in range(n):
    for j in range(n):
        if board[i][j] in ['R', 'G']:
            board[i][j] = 'RG'

normal, blind = 0, 0

for i in range(n):
    for j in range(n):
        if graph[i][j] != '.':
            now = graph[i][j]
            dfs(i, j, graph)
            normal += 1
        if board[i][j] != '.':
            now = board[i][j]
            dfs(i, j, board)
            blind += 1

print(normal, blind)