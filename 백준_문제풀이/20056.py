from copy import deepcopy

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

n, m, k = map(int, input().split())

graph = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    r, c, w, s, d = map(int, input().split())
    if w:
        graph[r - 1][c - 1].append((w, s, d))

for case in range(k):
    graph_copy = [[[] for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if graph[x][y]:
                for k in range(len(graph[x][y])):
                    w, s, d = graph[x][y][k]
                    nx, ny = x + dx[d] * s, y + dy[d] * s
                    nx = (nx + n) % n
                    ny = (ny + n) % n
                    graph_copy[nx][ny].append((w, s, d))


                
    for x in range(n):
        for y in range(n):
            if len(graph_copy[x][y]) >= 2:
                w, s, d = 0, 0, 0
                idx = len(graph_copy[x][y])
                for k in range(idx):
                    tmp_w, tmp_s, tmp_d = graph_copy[x][y][k]
                    w += tmp_w
                    s += tmp_s
                    d += tmp_d % 2
                w = w // 5
                s = s // len(graph_copy[x][y])
                graph_copy[x][y] = []
                if w:
                    if d == 0 or d == idx:
                        for i in range(4):
                            graph_copy[x][y].append((w, s, i * 2))
                    else:
                        for i in range(4):
                            graph_copy[x][y].append((w, s, i * 2 + 1))

    graph = deepcopy(graph_copy)


result = 0
for x in range(n):
    for y in range(n):
        if graph[x][y]:
            for k in range(len(graph[x][y])):
                result += graph[x][y][k][0]

print(result)