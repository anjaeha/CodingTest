# 낚시왕 한칸 이동 -> 낚시 -> 상어 이동

r, c, m = map(int, input().split())
graph = [[0] * c for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(m):
    x, y, s, d, z = map(int, input().split()) # 좌표 (x, y), 속력, 이동방향, 크기
    if d == 1 or d == 2: # 상하
        graph[x - 1][y - 1] = [s % (2 * r - 2), d - 1, z]
    else:
        graph[x - 1][y - 1] = [s % (2 * c - 2), d - 1, z]

def fishing(idx):
    global result
    for x in range(r):
        if graph[x][idx]:
            result += graph[x][idx][2]
            graph[x][idx] = 0
            return

def shark_move():
    global graph
    new_graph = [[0] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if graph[x][y]:
                now = graph[x][y]
                sx, sy, d = x, y, now[1]
                for i in range(now[0]):
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
                    if new_graph[sx][sy][2] < now[2]:
                        new_graph[sx][sy] = [now[0], d, now[2]]
                else:
                    new_graph[sx][sy] = [now[0], d, now[2]]
    graph = new_graph

result = 0
for idx in range(c):
    fishing(idx)
    shark_move()

print(result)