from collections import deque

t = int(input())
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

            if 0 <= nx < n and 0 <= ny < m and s[nx][ny] == 1:
                q.append((nx, ny))
                s[nx][ny] = 0


for case in range(t):
    m, n, k = map(int, input().split())
    s = [[0] * m for _ in range(n)]

    for i in range(k):
        a, b = map(int, input().split())
        s[b][a] = 1


    cnt = 0
    for i in range(n):
        for j in range(m):
            if s[i][j] == 1:
                bfs(i, j)
                s[i][j] = 0
                cnt += 1

    print(cnt)

"""
import sys
sys.setrecursionlimit(10 ** 4)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    graph[x][y] = 0

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1:
                dfs(nx, ny)


t = int(input())

for tc in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    for i in range(k):
        y, x = map(int, input().split())
        graph[x][y] = 1

    cnt = 0
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 1:
                dfs(x, y)
                cnt += 1
    print(cnt)
"""