import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    s[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if s[nx][ny] == 1:
            dfs(nx, ny)


for case in range(t):
    m, n, k = map(int, input().split())
    s = [[0] * m for _ in range(n)]
    cnt = 0
    for i in range(k):
        x, y = map(int, input().split())
        s[y][x] = 1


    for i in range(n):
        for j in range(m):
            if s[i][j] == 1:
                cnt += 1
                dfs(i, j)


    print(cnt)