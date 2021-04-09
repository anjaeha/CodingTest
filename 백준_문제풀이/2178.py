import sys
from collections import deque
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int,input().split())
s = []

for i in range(n):
    s.append(list(map(int, input().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if s[nx][ny] == 1:
                s[nx][ny] = s[x][y]  + 1
                q.append((nx, ny))
    

bfs(0, 0)
print(s[n-1][m-1])