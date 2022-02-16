from collections import deque

def check():
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0 and not visit[i][j]:
                bfs(i, j)
                count += 1
    return count >= 2

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m:
                if not visit[nx][ny] and graph[nx][ny] > 0:
                    visit[nx][ny] = True
                    q.append((nx, ny))

def all_melt():
    SUM = 0
    for i in range(n):
        SUM += sum(graph[i])
    return SUM == 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

year = 0
flag = False
while 1:
    visit = [[False] * m for _ in range(n)]
    if check():
        break
    if all_melt():
        flag = True
        break
    year += 1
    board = [[0] * m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            cnt = 0
            if graph[x][y] > 0:
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if 0 <= nx < n and 0 <= ny < m:
                        if graph[nx][ny] == 0:
                            cnt += 1
            board[x][y] = graph[x][y] - cnt
            if board[x][y] < 0:
                board[x][y] = 0
    graph = board

if not flag:
    print(year)
else:
    print(0)