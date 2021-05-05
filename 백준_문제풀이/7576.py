import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


s = []
for i in range(n):
    s.append(list(map(int, input().split())))
    
q = deque()

for i in range(n):
    for j in range(m):
        if s[i][j] == 1:
            q.append((i, j))

def bfs():
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if s[nx][ny] == -1:
                continue

            if s[nx][ny] == 0:
                s[nx][ny] = s[x][y] + 1
                q.append((nx, ny))

bfs()

flag = True
day = -1
for i in range(n):
    for j in range(m):
        day = max(day, s[i][j])
        if s[i][j] == 0:
            flag = False

if flag == False:
    print(-1)
else:
    print(day - 1)