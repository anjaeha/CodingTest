import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

m, n = map(int, input().split())
s = []
for i in range(n):
    s.append(list(map(int, input().split())))

q = deque()
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


for i in range(n):
    for j in range(m):
        if s[i][j] == 1:
            q.append((i, j))

bfs()

isTrue = True
day = 0
for i in range(n):
    for j in range(m):
        if s[i][j] == 0:
            isTrue = False
        day = max(day, s[i][j])

if isTrue:
    print(day - 1)
else:
    print(-1)
