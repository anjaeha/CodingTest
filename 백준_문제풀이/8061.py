from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


s = []
q = deque()
for i in range(n):
    s.append(list(input().strip()))

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and s[nx][ny] == "0":
                s[nx][ny] = int(s[x][y]) + 1
                q.append([nx, ny])



for i in range(n):
    for j in range(m):
        if s[i][j] == '1':
            s[i][j] = 0
            q.append([i, j])

bfs()

for i in range(n):
    for j in range(m):
        print(s[i][j], end = ' ')

    print()