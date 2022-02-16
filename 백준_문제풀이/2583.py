import sys
sys.setrecursionlimit(10 ** 4)

def dfs(x, y):
    global cnt
    graph[x][y] = 1
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:
                dfs(nx, ny)
                cnt += 1

n, m, k = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = [[0] * m for _ in range(n)]
for i in range(k):
    y1, x1, y2, x2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            graph[x][y] = 1

answer = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            cnt = 1
            dfs(i, j)
            answer.append(cnt)
answer.sort()
print(len(answer))
print(*answer)