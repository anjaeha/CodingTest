from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)] # 빈칸 - 0, 벽 - 1, 바이러스 - 2

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

zero_pos = []
virus_pos = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            zero_pos.append((i, j))
        elif graph[i][j] == 2:
            virus_pos.append((i, j))

candi = [] # 벽을 세울 수 있는 위치
visit = [False] * len(zero_pos)
temp = []
def make_candi(depth):
    if depth == 3:
        candi.append(list(temp))
        return
    for i in range(len(zero_pos)):
        if visit[i]:
            continue

        visit[i] = True
        temp.append(zero_pos[i])
        make_candi(depth + 1)
        temp.pop()
        for j in range(i + 1, len(zero_pos)):
            visit[j] = False

make_candi(0)

def check():
    global MAX,board
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                cnt += 1
    MAX = max(MAX, cnt)

def spread():
    q = virus_pos[:]
    q = deque(q)
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 0:
                    q.append((nx, ny))
                    board[nx][ny] = 2

MAX = -1
for i in range(len(candi)):
    temp = candi[i]
    board = [item[:] for item in graph]
    for x, y in temp:
        board[x][y] = 2
    spread()
    check()

print(MAX)