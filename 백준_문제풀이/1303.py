import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
s = [list(input().strip()) for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    cnt = 1
    q = deque()
    q.append((x, y))
    color = s[x][y]
    s[x][y] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue

            if s[nx][ny] == color:
                q.append((nx, ny))
                cnt += 1
                s[nx][ny] = 0

    if color == 'W':
        white.append(cnt)
    else:
        black.append(cnt)




black = []
white = []

for i in range(m):
    for j in range(n):
        if s[i][j] != 0:
            bfs(i, j)

w = 0
b = 0

for i in black:
    b += i ** 2

for i in white:
    w += i ** 2

print(w, b)