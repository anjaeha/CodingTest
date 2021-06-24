import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]

def dfs(x, y):
    s[x][y] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and s[nx][ny] == 1:
            s[nx][ny] = 0
            dfs(nx, ny)


while 1:
    m, n = map(int, input().split())
    if n == 0 and m == 0:
        break

    s = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if s[i][j] == 1:
                dfs(i, j)
                cnt += 1

    print(cnt)