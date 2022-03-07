n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find(idx, x, y, SUM):
    global MAX
    if idx == 4:
        MAX = max(MAX, SUM)
        return

    if SUM + (4 - idx) * mNumber <= MAX:
        return

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if not visit[nx][ny]:
                visit[nx][ny] = True
                find(idx + 1, nx, ny, SUM + graph[nx][ny])
                visit[nx][ny] = False

                if idx == 2:
                    visit[nx][ny] = True
                    find(idx + 1, x, y, SUM + graph[nx][ny])
                    visit[nx][ny] = False


mNumber = -1
for i in range(n):
    for j in range(m):
        mNumber = max(mNumber, graph[i][j])


visit = [[False] * m for _ in range(n)]
MAX = -1
for i in range(n):
    for j in range(m):
        visit[i][j] = True
        find(1, i, j, graph[i][j])
        visit[i][j] = False

print(MAX)