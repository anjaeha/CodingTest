from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def bfs(x, y):
    global board
    q = deque()
    q.append((x, y))
    SUM = [(x, y)]
    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < n:
                if not visit[nx][ny]:
                    if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                        visit[nx][ny] = True
                        q.append((nx, ny))
                        SUM.append((nx, ny))
    count = 0
    for x, y in SUM:
        count += graph[x][y]
    for x, y in SUM:
        board[x][y] = count // len(SUM)


idx = 0
while 1:
    visit = [[False] * n for _ in range(n)]
    board = [i[:] for i in graph]
    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                visit[i][j] = True
                bfs(i, j)

    if board == graph:
        break

    idx += 1
    graph = board
print(idx)