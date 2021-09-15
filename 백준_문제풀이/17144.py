n, m, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 확산
def spread():
    s = [[0] * m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if graph[x][y] > 0:
                count = []
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != -1:
                        count.append((nx, ny))
                temp = graph[x][y] // 5
                s[x][y] += graph[x][y] - (temp * len(count))
                for i, j in count:
                    s[i][j] += temp
    return s

# 공기청정기 위쪽 작동
def move_up(x, y):
    # 아래 방향
    for i in range(x - 1, 0, -1):
        graph[i][0] = graph[i - 1][0]
    # 왼쪽 방향
    for i in range(m - 1):
        graph[0][i] = graph[0][i + 1]
    # 위쪽 방향
    for i in range(x):
        graph[i][m - 1] = graph[i + 1][m - 1]
    # 오른쪽 방향
    for i in range(m - 1, 0, - 1):
        graph[x][i] = graph[x][i - 1]




def move_down(x, y):
    # 위 방향
    for i in range(x + 1, n - 1):
        graph[i][0] = graph[i + 1][0]
    # 왼쪽 방향
    for i in range(m - 1):
        graph[n - 1][i] = graph[n - 1][i + 1]
    # 아래 방향
    for i in range(n - 1, x - 1, - 1):
        graph[i][m - 1] = graph[i - 1][m - 1]
    # 오른쪽 방향
    for i in range(m - 1, 0, -1):
        graph[x][i] = graph[x][i - 1]
    

air = []
for i in range(n):
    if graph[i][0] == -1:
        up = [i, 0]
        down = [i + 1, 0]
        break

for case in range(t):       
    graph = spread()
    move_up(up[0], up[1])
    move_down(down[0], down[1])
    graph[up[0]][up[1]] = -1
    graph[down[0]][down[1]] = -1


result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] > 0:
            result += graph[i][j]

print(result)