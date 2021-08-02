import sys
sys.setrecursionlimit(10**5)
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
    if x < 0 or y < 0 or x >= n or y >= m or graph[x][y] == 9:
        return
    if d == 'U':
        visit[x][y] = 1
        if graph[x][y] == 0:
            dfs(x-1, y, 'U')
        elif graph[x][y] == 1:
            return
        elif graph[x][y] == 2:
            return
        elif graph[x][y] == 3:
            dfs(x, y + 1, 'R')
        elif graph[x][y] == 4:
            dfs(x, y - 1, 'L')
    elif d == 'D':
        visit[x][y] = 1
        if graph[x][y] == 0:
            dfs(x+1, y, 'D')
        elif graph[x][y] == 1:
            return
        elif graph[x][y] == 2:
            return
        elif graph[x][y] == 3:
            dfs(x, y-1, 'L')
        elif graph[x][y] == 4:
            dfs(x, y + 1, 'R')
    elif d == 'R':
        visit[x][y] = 1
        if graph[x][y] == 0:
            dfs(x, y + 1, 'R')
        elif graph[x][y] == 2:
            return
        elif graph[x][y] == 1:
            return
        elif graph[x][y] == 3:
            dfs(x-1, y, 'U')
        elif graph[x][y] == 4:
            dfs(x+1, y, 'D')
    elif d == 'L':
        visit[x][y] = 1
        if graph[x][y] == 0:
            dfs(x, y - 1, 'L')
        elif graph[x][y] == 2:
            return
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

# 다음과 같이 작성하면 됨!
"""
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visit = [[0] * m for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def search(x, y, d):
    while 1:
        x = x + dx[d]
        y = y + dy[d]

        if x < 0 or x >= n or y < 0 or y >= m or arr[x][y] == 9:
            break
        
        visit[x][y] = 1

        if arr[x][y] == 1 and (d == 0 or d == 2) or arr[x][y] == 2 and (d == 1 or d == 3):
            break
        elif arr[x][y] == 3:
            if d == 0:
                d = 3
            elif d == 1:
                d = 2
            elif d == 2:
                d = 1
            elif d == 3:
                d = 0
        elif arr[x][y] == 4:
            if d == 0:
                d = 1
            elif d == 1:
                d = 0
            elif d == 2:
                d = 3
            elif d == 3:
                d = 2



for i in range(n):
    for j in range(m):
        if arr[i][j] == 9:
            visit[i][j] = 1
            for d in range(4):
                search(i, j, d)
    
count = 0
for i in range(n):
    for j in range(m):
        if visit[i][j] == 1:
            count += 1

print(count)
"""