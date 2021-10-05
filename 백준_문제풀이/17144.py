
n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    if graph[i][0] == -1:
        airU = i
        airD = i + 1
        break

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def spread():
    s = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                temp = 0
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]

                    if 0 <= nx < n and 0 <= ny < m and not ((nx == airU and ny == 0) or (nx == airD and ny == 0)):
                        s[nx][ny] += graph[i][j] // 5
                        temp += graph[i][j] // 5
                s[i][j] += graph[i][j] - temp
    s[airU][0] = -1
    s[airD][0] = -1
    return s

def move():
    for i in range(airU - 1, 0, -1):
        graph[i][0] = graph[i - 1][0]
    for i in range(m - 1):
        graph[0][i] = graph[0][i + 1]
    for i in range(airU):
        graph[i][m - 1] = graph[i + 1][m - 1]
    for i in range(m - 1, 1, -1):
        graph[airU][i] = graph[airU][i - 1]
    graph[airU][1] = 0

    for i in range(airD + 1, n - 1):
        graph[i][0] = graph[i + 1][0]
    for i in range(m - 1):
        graph[n - 1][i] = graph[n - 1][i + 1]
    for i in range(n - 1, airD, - 1):
        graph[i][m - 1] = graph[i - 1][m - 1]
    for i in range(m - 1, 1, -1):
        graph[airD][i] = graph[airD][i - 1]
    graph[airD][1] = 0


while k:
    graph = spread()
    move()
    k -= 1

result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] > 0:
            result += graph[i][j]
print(result)