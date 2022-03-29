def check():
    for x, y in search_pos:
        if board[x][y] < k:
            return False
    return True

def border(): # 테두리 온도 감소
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

def machine_running(): # 온풍기 가동
    for x, y, dir in machine:
        arr = [[] for _ in range(6)]
        if dir == 1: # 오른쪽으로 온풍기 발사
            arr[5].append((x, y + 1))
            for idx in range(5, 0, -1):
                for r, c in arr[idx]:
                    if (r - 1, c) not in wall[2] and (r - 1, c) not in wall[0]: # 아래나 오른쪽에 벽 있으면 못감
                        if 0 <= (r - 1) < n and 0 <= (c + 1) < m and (r - 1, c + 1) not in arr[idx - 1]:
                            arr[idx - 1].append((r - 1, c + 1))
                    if (r, c) not in wall[0]: # 오른쪽에 벽 있으면 못감
                        if 0 <= r < n and 0 <= c + 1 < m and (r, c + 1) not in arr[idx - 1]:
                            arr[idx - 1].append((r, c + 1))
                    if (r + 1, c) not in wall[3] and (r + 1, c) not in wall[0]: # 위에나 오른쪽에 벽 있으면 못감
                        if 0 <= r + 1 < n and 0 <= c + 1 < m and (r + 1, c + 1) not in arr[idx - 1]:
                            arr[idx - 1].append((r + 1, c + 1))
        elif dir == 2: # 왼쪽으로 온풍기 발사
            arr[5].append((x, y - 1))
            for idx in range(5, 0, -1):
                for r, c in arr[idx]:
                    if (r - 1, c) not in wall[1] and (r - 1, c) not in wall[2]:
                        if 0 <= r - 1 < n and 0 <= c - 1 < m and (r - 1, c - 1) not in arr[idx - 1]:
                            arr[idx - 1].append((r - 1, c - 1))
                    if (r, c) not in wall[1]:
                        if 0 <= r < n and 0 <= c - 1 < m and (r, c - 1) not in arr[idx - 1]:
                            arr[idx - 1].append((r, c - 1))
                    if (r + 1, c) not in wall[1] and (r + 1, c) not in wall[3]:
                        if 0 <= r + 1 < n and 0 <= c - 1 < m and (r + 1, c - 1) not in arr[idx - 1]:
                            arr[idx - 1].append((r + 1, c - 1))
        elif dir == 3: # 위쪽으로 온풍기 발사
            arr[5].append((x - 1, y))
            for idx in range(5, 0, -1):
                for r, c in arr[idx]:
                    if (r, c - 1) not in wall[3] and (r, c - 1) not in wall[0]:
                        if 0 <= r - 1 < n and 0 <= c - 1 < m and (r - 1, c - 1) not in arr[idx - 1]:
                            arr[idx - 1].append((r - 1, c - 1))
                    if (r, c) not in wall[3]:
                        if 0 <= r - 1 < n and 0 <= c < m and (r - 1, c) not in arr[idx - 1]:
                            arr[idx - 1].append((r - 1, c))
                    if (r, c + 1) not in wall[1] and (r, c + 1) not in wall[3]:
                        if 0 <= r - 1 < n and 0 <= c + 1 < m and (r - 1, c + 1) not in arr[idx - 1]:
                            arr[idx - 1].append((r - 1, c + 1))
        elif dir == 4: # 아래쪽으로 온풍기 발사
            arr[5].append((x + 1, y))
            for idx in range(5, 0, -1):
                for r, c in arr[idx]:
                    if (r, c - 1) not in wall[0] and (r, c - 1) not in wall[2]:
                        if 0 <= r + 1 < n and 0 <= c - 1 < m and (r + 1, c - 1) not in arr[idx - 1]:
                            arr[idx - 1].append((r + 1, c - 1))
                    if (r, c) not in wall[2]:
                        if 0 <= r + 1 < n and 0 <= c < m and (r + 1, c) not in arr[idx - 1]:
                            arr[idx - 1].append((r + 1, c))
                    if (r, c + 1) not in wall[1] and (r, c + 1) not in wall[2]:
                        if 0 <= r + 1 < n and 0 <= c + 1 < m and (r + 1, c + 1) not in arr[idx - 1]:
                            arr[idx - 1].append((r + 1, c + 1))
        for idx in range(1, 6):
            for x, y in arr[idx]:
                board[x][y] += idx

n, m, k = map(int, input().split()) # 그래프 (R, C), 조사하는 칸의 온도가 K이상이면 종료
graph = [list(map(int, input().split())) for _ in range(n)] # 빈칸0, (우, 좌, 상, 하), 조사해야하는 칸5
board = [[0] * m for _ in range(n)] # 온도 확인 그래프

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

search_pos = []
machine = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 5:
            search_pos.append((i, j))
        elif 1 <= graph[i][j] <= 4:
            machine.append((i, j, graph[i][j]))

w = int(input())
wall = [[] for _ in range(4)] # 벽의 위치를 동, 서, 남, 북으로 재설정
for _ in range(w):
    x, y, t = map(int, input().split()) # 벽의 위치, 0이면 위에있고, 1이면 오른쪽에 있다.
    x, y = x - 1, y - 1
    if t == 1:
        wall[0].append((x, y)) # 오른쪽에 벽 있음
        wall[1].append((x, y + 1)) # 왼쪽에 벽 있음
    else:
        wall[3].append((x, y)) # 위에 벽이 있음
        wall[2].append((x - 1, y)) # 밑에 벽이 있음

def spread(): # 온도 퍼지기
    global board
    new_board = [i[:] for i in board]
    for x in range(n):
        for y in range(m):
            if board[x][y] >= 4:
                for d in range(4): # 위 아래 왼쪽 오른쪽
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if 0 <= nx < n and 0 <= ny < m:
                        if d == 0:
                            if (x, y) in wall[3]:
                                continue
                        elif d == 1:
                            if (x, y) in wall[2]:
                                continue
                        elif d == 2:
                            if (x, y) in wall[1]:
                                continue
                        elif d == 3:
                            if (x, y) in wall[0]:
                                continue
                        if board[x][y] > board[nx][ny]:
                            new_board[x][y] -= (board[x][y] - board[nx][ny]) // 4
                            new_board[nx][ny] += (board[x][y] - board[nx][ny]) // 4
    board = new_board

cnt = 0
while 1:
    machine_running()
    spread()
    border()
    cnt += 1
    if check():
        break
    if cnt > 100:
        break

print(cnt)