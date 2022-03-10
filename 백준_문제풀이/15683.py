n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

direct = [[], [[0], [1], [2], [3]], [[0, 2], [1, 3]], [[0, 1], [1, 2], [2, 3], [3, 0]], [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]], [[0, 1, 2, 3]]]

camera = []
for i in range(n):
    for j in range(m):
        if graph[i][j] in [1,2,3,4,5]:
            camera.append((i, j, graph[i][j]))

def fill(x, y, d):
    for i in d:
        nx, ny = x, y
        while 1:
            nx = nx + dx[i]
            ny = ny + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != 6:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = '#'
                else:
                    break
            else:
                break



MIN = int(1e9)
def dfs(depth):
    global MIN, graph
    if depth == len(camera):
        MIN = min(MIN, check())
        return

    temp_graph = [i[:] for i in graph]
    x, y, dir = camera[depth]
    for i in direct[dir]:
        fill(x, y, i)
        dfs(depth + 1)
        graph = [i[:] for i in temp_graph]

def check():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                cnt += 1
    return cnt

dfs(0)
print(MIN)