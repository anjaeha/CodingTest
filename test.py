from collections import deque

t = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and s[nx][ny] == 1:
                q.append((nx, ny))
                s[nx][ny] = 0


for case in range(t):
    m, n, k = map(int, input().split())
    s = [[0] * m for _ in range(n)]

    for i in range(k):
        a, b = map(int, input().split())
        s[b][a] = 1


    cnt = 0
    for i in range(n):
        for j in range(m):
            if s[i][j] == 1:
                bfs(i, j)
                s[i][j] = 0
                cnt += 1

    print(cnt)