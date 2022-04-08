n, m, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    if graph[i][0] == -1:
        up_x = i
        down_x = i + 1
        graph[i][0] = 0
        graph[i + 1][0] =0
        break


def spread():
    global graph
    new_graph = [i[:] for i in graph]
    for x in range(n):
        for y in range(m):
            if graph[x][y] >= 5:
                count = 0
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if 0 <= nx < n and 0 <= ny < m:
                        if (nx, ny) != (up_x, 0) and (nx, ny) != (down_x, 0):
                            new_graph[nx][ny] += graph[x][y] // 5
                            count += graph[x][y] // 5
                new_graph[x][y] -= count
    graph = new_graph

def rotate():
    for x in range(up_x - 1, 0, -1):
        graph[x][0] = graph[x - 1][0]
    for y in range(m - 1):
        graph[0][y] = graph[0][y + 1]
    for x in range(up_x):
        graph[x][m - 1] = graph[x + 1][m - 1]
    for y in range(m - 1, 0, -1):
        graph[up_x][y] = graph[up_x][y - 1]

    for x in range(down_x + 1, n - 1):
        graph[x][0] = graph[x + 1][0]
    for y in range(m - 1):
        graph[n - 1][y] = graph[n - 1][y + 1]
    for x in range(n - 1, down_x, -1):
        graph[x][m - 1] = graph[x - 1][m - 1]
    for y in range(m - 1, 0, -1):
        graph[down_x][y] = graph[down_x][y - 1]

for _ in range(t):
    spread()
    rotate()

result = 0
for i in range(n):
    for j in range(m):
        result += graph[i][j]

print(result)