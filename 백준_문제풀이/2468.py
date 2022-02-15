from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check(x):
    board = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > x:
                board[i][j] = 1
    return board

def search(x, y):
    q = deque()
    q.append((x, y))
    board[x][y] = 0
    visit = [[False] * n for _ in range(n)]
    visit[x][y] = True

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 1 and not visit[nx][ny]:
                    q.append((nx, ny))
                    visit[nx][ny]
                    board[nx][ny] = 0


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

MAX = 0
for i in range(n):
    for j in range(n):
       MAX = max(MAX, graph[i][j])


result = 0
for i in range(MAX):
    board = check(i)
    cnt = 0
    for x in range(n):
        for y in range(n):
            if board[x][y] == 1:
                search(x, y)
                cnt += 1
    result = max(result, cnt)

print(result)