import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0, -1, -1 ,1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

n, m = map(int, input().split())
board = []
check = [[-1] * m for _ in range(n)]

for i in range(n):
    board.append(list(map(int, input().split())))

q = deque()

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            q.append((i, j))
            check[i][j] = 0
ans = 0
while q:
    x, y = q.popleft()

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and check[nx][ny] == -1:
            check[nx][ny] = check[x][y] + 1
            ans = max(ans, check[nx][ny])
            q.append((nx, ny))

print(ans)