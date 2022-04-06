n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

dir = [[], [[0], [1], [2], [3]], [[0, 2], [1, 3]], [[0, 1], [1, 2], [2, 3], [3, 0]], [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]], [[0, 1, 2, 3]]]

cctv_pos = []
cctv_cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] in [1,2,3,4,5]:
            cctv_pos.append((i, j, graph[i][j]))
            cctv_cnt += 1

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
result = int(1e9)
def dfs(depth):
    global result, graph
    if depth == cctv_cnt:
        cnt = 0
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 0:
                    cnt += 1
        result = min(result, cnt)
        return

    temp_graph = [i[:] for i in graph]
    x, y, d = cctv_pos[depth]
    for i in dir[d]:
        fill(x, y, i)
        dfs(depth + 1)
        graph = [i[:] for i in temp_graph]

dfs(0)
print(result)