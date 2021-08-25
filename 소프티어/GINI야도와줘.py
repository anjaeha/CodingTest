import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
visit = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'W':
            startx, starty = i, j
            visit[i][j] = True
            graph[i][j] = 0
        elif graph[i][j] == 'H':
            endx, endy = i, j

def find_cloud():
    cloud = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == '*':
                cloud.append((i, j))
    return cloud

def move_cloud(array):
    for x, y in array:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 'X' or graph[nx][ny] == 'H':
                    continue
                else:
                    graph[nx][ny] = '*'

def bfs(x, y):
    global answer
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        cloud = find_cloud()
        move_cloud(cloud)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if (graph[nx][ny] == '.') and visit[nx][ny] == False:
                    q.append((nx, ny))
                    visit[nx][ny] = True
                    graph[nx][ny] = graph[x][y] + 1
                elif graph[nx][ny] == 'H':
                    graph[nx][ny] = graph[x][y] + 1
                    answer = graph[nx][ny]
                    return


answer = 0
bfs(startx, starty)
print(graph)
print(answer if answer else "FAIL")