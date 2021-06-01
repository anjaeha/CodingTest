from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    sheep_cnt, wolf_cnt = 0, 0
    a[i][j] = 1

    while q:
        x, y = q.popleft()

        if s[x][y] == 'v':
            wolf_cnt += 1
        elif s[x][y] == 'k':
            sheep_cnt += 1


        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                if s[nx][ny] != '#' and not a[nx][ny]:
                    q.append((nx, ny))
                    a[nx][ny]= 1

    if wolf_cnt >= sheep_cnt:
        sheep_cnt = 0
    else:
        wolf_cnt = 0

    return sheep_cnt, wolf_cnt
    
r, c = map(int, input().split())
s = [list(input().strip()) for _ in range(r)]
a = [[0]* c for _ in range(r)]

sheep, wolf = 0, 0
for i in range(r):
    for j in range(c):
        if s[i][j] != '#' and not a[i][j]:
            o, w = bfs(i, j)
            sheep += o
            wolf += w


print(sheep, wolf)