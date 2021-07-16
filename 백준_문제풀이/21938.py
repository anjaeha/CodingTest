import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
s = [[] for _ in range(n)]

for case in range(n):
    temp = list(map(int, input().split()))
    for i in range(0, m * 3, 3):
        k = (temp[i] + temp[i+1] + temp[i+2]) // 3
        s[case].append(k)
        
T = int(input())

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if s[nx][ny] >= T:
                q.append((nx, ny))
                s[nx][ny] = 0

cnt = 0
for i in range(n):
    for j in range(m):
        if s[i][j] >= T:
            bfs(i, j)
            cnt += 1

print(cnt)