import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global cnt
    cnt += 1
    visit[x][y] = 1

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
    
        if nx <= 0 or nx > n or ny <= 0 or ny > m:
            continue

        if s[nx][ny] == 1 and visit[nx][ny] == 0:
            dfs(nx, ny)


n, m, k = map(int, input().split())

s = [[0] * (m+1) for _ in range(n+1)]
visit = [[0] * (m+1) for _ in range(n+1)]

for i in range(k):
    x, y = map(int, input().split())
    s[x][y] = 1
           
ans = []
for i in range(1, n+1):
    for j in range(1, m+1):
        if s[i][j] == 1 and visit[i][j] == 0:
            cnt = 0
            dfs(i, j)
            ans.append(cnt)

print(max(ans))