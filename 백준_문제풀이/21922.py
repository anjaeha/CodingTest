import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visit = [[0] * m for _ in range(n)]

air = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 9:
            visit[i][j] = 1
            air.append([i, j])

if air == []:
    print(0)
    exit()

def dfs(x, y, d):
    if x < 0 or y < 0 or x >= n or y >= m:
        return
    if d == 'U':
        visit[x][y] = 1
        if graph[x][y] == 0 or graph[x][y] == 1:
            dfs(x-1, y, 'U')
        elif graph[x][y] == 2:
            return
        elif graph[x][y] == 3:
            dfs(x, y + 1, 'R')
        elif graph[x][y] == 4:
            dfs(x, y - 1, 'L')
    elif d == 'D':
        visit[x][y] = 1
        if graph[x][y] == 0 or graph[x][y] == 1:
            dfs(x+1, y, 'D')
        elif graph[x][y] == 2:
            return
        elif graph[x][y] == 3:
            dfs(x, y-1, 'L')
        elif graph[x][y] == 4:
            dfs(x, y + 1, 'R')
    elif d == 'R':
        visit[x][y] = 1
        if graph[x][y] == 0 or graph[x][y] == 2:
            dfs(x, y + 1, 'R')
        elif graph[x][y] == 1:
            return
        elif graph[x][y] == 3:
            dfs(x-1, y, 'U')
        elif graph[x][y] == 4:
            dfs(x+1, y, 'D')
    elif d == 'L':
        visit[x][y] = 1
        if graph[x][y] == 0 or graph[x][y] == 2:
            dfs(x, y - 1, 'L')
        elif graph[x][y] == 1:
            return
        elif graph[x][y] == 3:
            dfs(x+1, y, 'D')
        elif graph[x][y] == 4:
            dfs(x-1, y, 'U')


for airx, airy in air:
    dfs(airx-1, airy, 'U')
    dfs(airx+1, airy, 'D')
    dfs(airx, airy+1, 'R')
    dfs(airx, airy-1, 'L')

count = 0
for i in range(n):
    for j in range(m):
        if visit[i][j] == 1:
            count += 1

print(count)

# 재귀오류 발생.