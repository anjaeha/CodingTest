from copy import deepcopy

n, m, k = map(int, input().split())
board = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    r, c, m, s, d = map(int, input().split())

    if m != 0:
        board[r - 1][c - 1].append([m, s, d])

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(k):
    n_board = [[[] for _ in range(n)] for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if board[x][y] != []:
                for k in range(len(board[x][y])):
                    nn, ss, dd = board[x][y][k]
                    nx = x + dx[dd] * ss
                    ny = y + dy[dd] * ss
                    nx = (nx + n) % n
                    ny = (ny + n) % n
                    n_board[nx][ny].append((nn, ss, dd))

    for x in range(n):
        for y in range(n):
            if len(n_board[x][y]) >= 2:
                mm, ss, dd = 0, 0, []
                cnt = len(n_board[x][y])
                for c in range(cnt):
                    mm += n_board[x][y][c][0]
                    ss += n_board[x][y][c][1]
                    dd.append(n_board[x][y][c][2] % 2)
                mm //= 5
                ss //= cnt
                n_board[x][y] = []
                if mm != 0:
                    if sum(dd) == 0 or sum(dd) == cnt:
                        for i in range(4):
                            n_board[x][y].append((mm, ss, i * 2))
                    else:
                        for i in range(4):
                            n_board[x][y].append((mm, ss, i * 2 + 1))

    board = deepcopy(n_board)


result = 0
for x in range(n):
    for y in range(n):
        if board[x][y] != []:
            for k in range(len(board[x][y])):
                result += board[x][y][k][0]

print(result)