dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
from collections import deque
def bfs(x, y):
    visit = [[False] * m for _ in range(n)]
    visit[x][y] = True
    graph[x][y] = 0
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and not visit[nx][ny]:
                    q.append((nx, ny))
                    visit[nx][ny] = True
                    graph[nx][ny] = 0

def dfs(x, y):
    graph[x][y] = 0

    for d in range(8):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1:
                dfs(nx, ny)

while 1:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]

    answer = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i, j)   # dfs(i, j)로도 가능하다
                answer += 1

    print(answer)