from collections import deque

dx = [0, 1, 0, -1] # 동, 남, 서, 북
dy = [1, 0, -1, 0]

def score(x, y):
    q = deque()
    q.append((x, y))
    cnt = [(x, y)]
    visit[x][y] = True
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m:
                if not visit[nx][ny] and graph[nx][ny] == graph[x][y]:
                    visit[nx][ny] = True
                    q.append((nx, ny))
                    cnt.append((nx, ny))
    for x, y in cnt:
        board[x][y] = graph[x][y] * len(cnt)

def move():
    global result, sx, sy, sd
    x, y, d = sx, sy, sd
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < n and 0 <= ny < m:
        pass
    else:
        d = (d + 2) % 4 # 반대 방향으로 바꿈
        nx = x + dx[d]
        ny = y + dy[d]
    dice_move(d)
    result += board[nx][ny]
    if graph[nx][ny] > dice[6]:
        d = (d - 1) % 4
    elif graph[nx][ny] < dice[6]:
        d = (d + 1) % 4
    sx, sy, sd = nx, ny, d

def dice_move(dir):
    global dice
    if dir == 0: # 동쪽으로 굴리면
        dice = [dice[0], dice[4], dice[2], dice[1], dice[6], dice[5], dice[3]]
    elif dir == 1: # 남쪽으로 굴리면
        dice = [dice[0], dice[2], dice[6], dice[3], dice[4], dice[1], dice[5]]
    elif dir == 2: # 서쪽으로 굴리면
        dice = [dice[0], dice[3], dice[2], dice[6], dice[1], dice[5], dice[4]]
    elif dir == 3: # 북쪽으로 굴리면
        dice = [dice[0], dice[5], dice[1], dice[3], dice[4], dice[6], dice[2]]

n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
board = [[0] * m for _ in range(n)] # 점수 획득 판
visit = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if not visit[i][j]:
            score(i, j)

sx, sy, sd = 0, 0, 0 # 시작 위치는 (0, 0) 방향은 동쪽
dice = [0, 1, 2, 3, 4, 5, 6]

result = 0
for _ in range(k):
    move()

print(result)