import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0 ,0, -1, 1]

n = int(input())
h = [list(map(int, input().split())) for _ in range(n)]
ans = []
count = -1

MAX = 0
for i in h:
    if MAX < max(i):
        MAX = max(i)

def bfs(i, j):
    q = deque()
    q.append((i, j))
    s[i][j] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if s[nx][ny] == 0:
                q.append((nx, ny))
                s[nx][ny] = 1
                

while count != MAX:
    cnt = 0
    count += 1
    s = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if h[i][j] <= count:
                s[i][j] = 1 # 잠김

    for i in range(n):
        for j in range(n):
            if s[i][j] == 0:
                bfs(i, j)
                cnt += 1
    
    ans.append(cnt)

print(max(ans))