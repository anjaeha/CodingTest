import sys
input = sys.stdin.readline
from collections import deque

r, c = map(int, input().split())
s = [list(input().strip()) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue

            if s[nx][ny] == 'S':
                flag = False
                print(0)
                exit()

            if s[nx][ny] == '.':
                s[nx][ny] = 'D'
            
flag = True
for i in range(r):
    for j in range(c):
        if s[i][j] == 'W':
            bfs(i, j)


print(1)
for i in range(r):
    for j in range(c):
        print(s[i][j], end = '')
    print()