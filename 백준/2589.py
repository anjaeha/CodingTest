from collections import deque

n, m = map(int, input().split())

s = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
result = 0

for i in range(n):
    s.append(list(map(str, input())))

def bfs(i, j):
    queue = deque()
    queue.append([i,j])
    max_n = 0

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0 and s[nx][ny] != 'W':
                visit[nx][ny] = 1
                s[nx][ny] = s[x][y] + 1
                max_n = max(max_n, s[nx][ny])
                queue.append([nx, ny])

    return max_n


for i in range(n):
    for j in range(m):
        if s[i][j] != 'W':
            visit = [[0] * m for _ in range(n)]
            s[i][j] = 0
            visit[i][j] = 1
            result = max(result, bfs(i, j))

print(result)