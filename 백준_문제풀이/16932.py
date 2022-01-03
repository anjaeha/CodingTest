from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

MAX = -1
visit = [[False] * m for _ in range(n)]
board = [[0] * m for _ in range(n)]

def bfs(x, y):
    q = deque()
    arr = deque()
    arr.append((x, y))
    q.append((x, y))
    count = 1
    visit[x][y] = True
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y  +dy[d]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and visit[nx][ny] == False:
                    count += 1
                    visit[nx][ny] = True
                    q.append((nx, ny))
                    arr.append((nx, ny))
    for x, y in arr:
        board[x][y] = arr
    return

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visit[i][j] == False:
            bfs(i, j)

MAX = -1
for i in range(n):
    for j in range(m):
        if board[i][j] != 0:
            continue
        temp = set()
        for d in range(4):
            nx = i + dx[d]
            ny = j + dy[d]

            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 0:
                    continue
                temp.update(board[nx][ny])
        MAX = max(MAX, len(temp) + 1)

print(MAX)