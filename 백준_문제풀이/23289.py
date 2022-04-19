n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
w = int(input())
wall = [[] for _ in range(4)]
board = [[0] * m for _ in range(n)] # 온도 표시

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(w):
    x, y, d = map(int, input().split())
    if d == 0: # 벽이 위에 있는 경우
        wall[0].append((x - 1, y - 1)) # 위쪽에 벽이 있음
        wall[1].append((x - 2, y - 1)) # 아래쪽에 벽이 있음
    else: # 오른쪽에 벽이 있는 경우
        wall[2].append((x - 1, y - 1)) # 오른쪽에 벽이 있음
        wall[3].append((x - 1, y)) # 왼쪽에 벽이 있음

check_pos = []
machine_pos = [[] for _ in range(5)]
for x in range(n):
    for y in range(m):
        if graph[x][y] == 5:
            check_pos.append((x, y))
        elif 0 < graph[x][y] < 5:
            machine_pos[graph[x][y]].append((x, y))

def machine_work(x, y, d):
    if d == 1: # 방향이 오른쪽인 온풍기
        now = [[] for _ in range(6)]
        now[5].append((x, y + 1))
        for idx in range(5, 1, -1):
            for r, c in now[idx]:
                if (r, c) not in wall[0] and (r - 1, c) not in wall[2] and 0 <= r - 1 < n and 0 <= c + 1 < m and (r - 1, c + 1) not in now[idx - 1]:
                    now[idx - 1].append((r - 1, c + 1))
                if (r, c) not in wall[2] and 0 <= r < n and 0 <= c + 1 < m and (r, c + 1) not in now[idx - 1]:
                    now[idx - 1].append((r, c + 1))
                if (r, c) not in wall[1] and (r + 1, c) not in wall[2] and 0 <= r + 1 < n and 0 <= c + 1 < m and (r + 1, c + 1) not in now[idx - 1]:
                    now[idx - 1].append((r + 1, c + 1))
    elif d == 2: # 방향이 왼쪽인 온풍기
        now = [[] for _ in range(6)]
        now[5].append((x, y - 1))
        for idx in range(5, 1, -1):
            for r, c in now[idx]:
                if (r, c) not in wall[0] and (r - 1, c) not in wall[3] and 0 <= r - 1 < n and 0 <= c - 1 < m and (r - 1, c - 1) not in now[idx - 1]:
                    now[idx - 1].append((r - 1, c - 1))
                if (r, c) not in wall[3] and 0 <= r < n and 0 <= c - 1 < m and (r, c - 1) not in now[idx - 1]:
                    now[idx - 1].append((r, c - 1))
                if (r, c) not in wall[1] and (r + 1, c) not in wall[3] and 0 <= r + 1 < n and 0 <= c - 1 < m and (r + 1, c - 1) not in now[idx - 1]:
                    now[idx - 1].append((r + 1, c - 1))
    elif d == 3: # 방향이 위인 온풍기
        now = [[] for _ in range(6)]
        now[5].append((x - 1, y))
        for idx in range(5, 1, -1):
            for r, c in now[idx]:
                if (r, c) not in wall[3] and (r, c - 1) not in wall[0] and 0 <= r - 1 < n and 0 <= c - 1 < m and (r - 1, c - 1) not in now[idx - 1]:
                    now[idx - 1].append((r - 1, c - 1))
                if (r, c) not in wall[0] and 0 <= r - 1 < n and 0 <= c < m and (r - 1, c) not in now[idx - 1]:
                    now[idx - 1].append((r - 1, c))
                if (r, c) not in wall[2] and (r, c + 1) not in wall[0] and 0 <= r - 1 < n and 0 <= c + 1 < m and (r - 1, c + 1) not in now[idx - 1]:
                    now[idx - 1].append((r - 1, c + 1))
    elif d == 4: # 방향이 아래인 온풍기
        now = [[] for _ in range(6)]
        now[5].append((x + 1, y))
        for idx in range(5, 1, -1):
            for r, c in now[idx]:
                if (r, c) not in wall[3] and (r, c - 1) not in wall[1] and 0 <= r + 1 < n and 0 <= c - 1 < m and (r + 1, c - 1) not in now[idx - 1]:
                    now[idx - 1].append((r + 1, c - 1))
                if (r, c) not in wall[1] and 0 <= r + 1 < n and 0 <= c < m and (r + 1, c) not in now[idx - 1]:
                    now[idx - 1].append((r + 1, c))
                if (r, c) not in wall[2] and (r, c + 1) not in wall[1] and 0 <= r + 1 < n and 0 <= c + 1 < m and (r + 1, c + 1) not in now[idx - 1]:
                    now[idx - 1].append((r + 1, c + 1))

    for idx in range(1, 6):
        for r, c in now[idx]:
            board[r][c] += idx

def tmp_control():
    global board
    temp_board = [i[:] for i in board]
    for x in range(n):
        for y in range(m):
            if board[x][y] >= 4:
                for d in range(4):
                    if (x, y) not in wall[d]:
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < n and 0 <= ny < m and board[x][y] > board[nx][ny]:
                            temp_board[x][y] -= (board[x][y] - board[nx][ny]) // 4
                            temp_board[nx][ny] += (board[x][y] - board[nx][ny]) // 4
    board = temp_board

def border():
    for i in range(n):
        if board[i][0] > 0:
            board[i][0] -= 1
        if board[i][m - 1] > 0:
            board[i][m - 1] -= 1
    for i in range(1, m - 1):
        if board[0][i] > 0:
            board[0][i] -= 1
        if board[n - 1][i] > 0:
            board[n - 1][i] -= 1

def check():
    for x, y in check_pos:
        if board[x][y] < k:
            return False
    return True

result = 0

while 1:
    for idx in range(1, 5):
        temp = machine_pos[idx]
        for i in range(len(temp)):
            x = temp[i][0]
            y = temp[i][1]
            machine_work(x, y, idx)
    tmp_control()
    border()
    result += 1
    if check() or result >= 101:
        break

print(result)