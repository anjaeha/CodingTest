import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def bfs(x, y):
    cnt = 0
    q = deque()
    q.append((x, y))
    s[x][y] = 0

    while q:
        cnt += 1
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if s[nx][ny] == 1:
                q.append((nx, ny))
                s[nx][ny] = 0

    return cnt

s = graph
size = []
for i in range(n):
    for j in range(m):
        if s[i][j] == 1:
            temp = bfs(i ,j)
            size.append(temp)


print(len(size))
print(max(size) if size else 0)