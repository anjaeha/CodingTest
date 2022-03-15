r, c, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]

for i in range(r):
    if graph[i][0] == -1: # 공기청정기 좌표
        up_x = i
        down_x = i + 1
        graph[i][0] = 0
        graph[i + 1][0] = 0
        break

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def spread():
    global graph
    new_graph = [i[:] for i in graph]
    for i in range(r):
        for j in range(c):
            if graph[i][j] >= 5: # 5 이상일때만 미세먼지 확산됨.
                cnt = 0
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]

                    if 0 <= nx < r and 0 <= ny < c:
                        if 0 <= graph[nx][ny] and (nx, ny) != (up_x, 0) and (nx, ny) != (down_x, 0):
                            new_graph[nx][ny] += graph[i][j] // 5
                            cnt += 1
                new_graph[i][j] -= graph[i][j] // 5 * cnt
    graph = new_graph

def activ():
    # 윗부분 공기순환
    for x in range(up_x - 1, 0, -1):
        graph[x][0] = graph[x - 1][0]
    for y in range(c - 1):
        graph[0][y] = graph[0][y + 1]
    for x in range(up_x):
        graph[x][c - 1] = graph[x + 1][c - 1]
    for y in range(c - 1, 0, -1):
        graph[up_x][y] = graph[up_x][y - 1]

    # 아래부분 공기순환
    for x in range(down_x + 1, r - 1):
        graph[x][0] = graph[x + 1][0]
    for y in range(c - 1):
        graph[r - 1][y] = graph[r - 1][y + 1]
    for x in range(r - 1, down_x, -1):
        graph[x][c - 1] = graph[x - 1][c - 1]
    for y in range(c - 1, 0, -1):
        graph[down_x][y] = graph[down_x][y - 1]

for _ in range(t):
    spread()
    activ()

result = 0
for i in range(r):
    for j in range(c):
        result += graph[i][j]

print(result)