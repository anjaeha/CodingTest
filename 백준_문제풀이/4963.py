import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def bfs(i, j):
    q = deque()
    q.append((i,j))
    while q:
        x, y = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue

            if s[nx][ny] == 1:
                q.append((nx, ny))
                s[nx][ny] = 0


while 1:
    w, h = map(int, input().split())
    cnt = 0
    if w == 0 and h == 0:
        break
    s = []
    for i in range(h):
        s.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if s[i][j] == 1:
                bfs(i, j)
                s[i][j] = 0
                cnt += 1

    print(cnt)