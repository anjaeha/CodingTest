from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

board = [list(map(str, input().strip())) for _ in range(12)]

def bfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 12 and 0 <= ny < 6:
            if board[x][y] == board[nx][ny] and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                q.append((nx, ny))


def fall():
    for j in range(6):
        bag = deque()
        for i in range(11, -1, -1):
            if board[i][j] != '.':
                bag.append(board[i][j])
        for i in range(11, -1, -1):
            if bag:
                board[i][j] = bag.popleft()
            else:
                board[i][j] = '.'



chk = False
answer = 0
while 1:
    visit = [[0] * 6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if board[i][j] != '.' and visit[i][j] == 0:
                visit[i][j] = 1
                q = deque([[i, j]])
                st = []

                while q:
                    now = q.popleft()
                    st.append(now)
                    bfs(now[0], now[1])
                if len(st) >= 4:
                    chk = True
                    for s in st:
                        board[s[0]][s[1]] = '.'
    fall()
    if not chk:
        break
    chk = False
    answer += 1
print(answer)