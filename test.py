import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
s = []
for i in range(n):
    s.append(list(map(int, input().strip())))


def bfs(a, b):
    q = deque()
    q.append((a, b))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if s[nx][ny] == 1:
                s[nx][ny] = s[x][y] + 1
                q.append((nx, ny))
                

bfs(0, 0)
print(s[n-1][m-1])