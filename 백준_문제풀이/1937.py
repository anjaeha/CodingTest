import sys
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
visit = [[0] * n for _ in range(n)]
cnt = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if visit[x][y] != 0:
        return visit[x][y]
        
    visit[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if s[x][y] < s[nx][ny]:
                visit[x][y] = max(visit[x][y], dfs(nx, ny) + 1)

    return visit[x][y]


for i in range(n):
    for j in range(n):
        cnt = max(cnt, dfs(i, j))

print(cnt)