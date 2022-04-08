r, c, m = map(int, input().split())
graph = [[0] * c for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(m):
    x, y, s, d, z = map(int, input().split())
    if (d - 1) in [0, 1]: # 위아래로 움직이는 경우에는
        graph[x - 1][y - 1] = [s % (r * 2 - 2), d - 1, z] # 속력 방향 크기
    elif (d - 1) in [2, 3]: # 좌우로 움직이는 경우에는
        graph[x - 1][y - 1] = [s % (c * 2 -  2), d - 1, z]

result = 0
def fishing(idx):
    global result
    for i in range(r):
        if graph[i][idx] != 0:
            result += graph[i][idx][2]
            graph[i][idx] = 0
            return

def shark_move():
    global graph
    new_graph = [[0] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if graph[x][y] != 0:
                s, d, z = graph[x][y] # 속력 방향 크기
                sx, sy = x, y
                for i in range(s):
                    nx = sx + dx[d]
                    ny = sy + dy[d]
                    if 0 <= nx < r and 0 <= ny < c:
                        pass
                    else:
                        d ^= 1
                        nx = sx + dx[d]
                        ny = sy + dy[d]
                    sx, sy = nx, ny
                if new_graph[sx][sy]:
                    if new_graph[sx][sy][2] > z:
                        pass
                    else:
                        new_graph[sx][sy] = [s, d, z]
                else:
                    new_graph[sx][sy] = [s, d, z]
    graph = new_graph

for idx in range(c):
    fishing(idx)
    shark_move()

print(result)