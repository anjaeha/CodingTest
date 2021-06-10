import sys
input = sys.stdin.readline

m, n = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(m)]
visit = [[-1] * n for _ in range(m)]
visit[m-1][n-1] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if visit[x][y] == -1:
        visit[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if s[x][y] > s[nx][ny]:
                visit[x][y] += dfs(nx, ny)

    return visit[x][y]


print(dfs(0, 0))