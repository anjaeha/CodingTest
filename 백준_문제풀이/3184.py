from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    visit = [[False] * m for _ in range(n)]
    visit[x][y] = True
    q = deque()
    q.append((x, y))
    temp_sheep, temp_wolf = 0, 0
    while q:
        x, y = q.popleft()
        if graph[x][y] == 'o':
            temp_sheep += 1
        elif graph[x][y] == 'v':
            temp_wolf += 1
        graph[x][y] = '.'
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != '#' and not visit[nx][ny]:
                    q.append((nx, ny))
                    visit[nx][ny] = True
    return temp_sheep, temp_wolf


n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]

sheep, wolf = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] in ['o', 'v']:
            temp_sheep, temp_wolf = bfs(i, j)
            if temp_sheep > temp_wolf:
                sheep += temp_sheep
            else:
                wolf += temp_wolf

print(sheep, wolf)