import sys
sys.setrecursionlimit(10 ** 4)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global count
    count += 1
    graph[x][y] = 0
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1:
                dfs(nx, ny)

n, m, k = map(int, input().split())

graph = [[0] * m for _ in range(n)]
for i in range(k):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = 1

MAX = -1
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            count = 0
            dfs(i, j)
            MAX = max(MAX, count)

print(MAX)