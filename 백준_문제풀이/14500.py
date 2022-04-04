n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, depth, result):
    global MAX
    if depth == 4:
        MAX = max(MAX, result)
        return

    if result + (4 - depth) * mNumber <= MAX:
        return

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
            visit[nx][ny] = True
            dfs(nx, ny, depth + 1, result + graph[nx][ny])
            visit[nx][ny] = False

            if depth == 2:
                visit[nx][ny] = True
                dfs(x, y, depth + 1, result + graph[nx][ny])
                visit[nx][ny] = False

mNumber = -1
for i in range(n):
    mNumber = max(mNumber, max(graph[i]))

MAX = -1
visit = [[False] * m for _ in range(n)]
for x in range(n):
    for y in range(m):
        visit[x][y] = True
        dfs(x, y, 1, graph[x][y])
        visit[x][y] = False

print(MAX)