graph = [[[] for _ in range(4)] for _ in range(4)]
smell = [[0] * 4 for _ in range(4)]
m, s = map(int, input().split()) # 물고기 수, 상어가 마법을 연습한 횟수
for _ in range(m):
    x, y, d = map(int, input().split())
    if graph[x - 1][y - 1]:
        graph[x - 1][y - 1].append(d - 1)
    else:
        graph[x - 1][y - 1] = [d - 1]

sx, sy = map(int, input().split()) # 상어의 위치
sx, sy = sx - 1, sy - 1

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

sdx = [-1, 0, 1, 0]
sdy = [0, -1, 0, 1]

def fish_move(): # 물고기 이동 시작
    global graph
    temp_graph = [[[] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            if graph[x][y]:
                for now in graph[x][y]:
                    for d in range(8):
                        nx = x + dx[now]
                        ny = y + dy[now]
                        if 0 <= nx < 4 and 0 <= ny < 4 and smell[nx][ny] == 0 and (nx, ny) != (sx, sy):
                            if temp_graph[nx][ny]:
                                temp_graph[nx][ny].append(now)
                            else:
                                temp_graph[nx][ny] = [now]
                            break
                        else:
                            now = (now - 1) % 8
                    else:
                        if temp_graph[x][y]:
                            temp_graph[x][y].append(now)
                        else:
                            temp_graph[x][y] = [now]
    graph = temp_graph

temp = []
candi = []
def make_candi(depth):
    if depth == 3:
        candi.append(list(temp))
        return

    for i in range(4):
        temp.append(i)
        make_candi(depth + 1)
        temp.pop()
make_candi(0)

def shark_move():
    global sx, sy
    move = [-1, -1] # 제외한 물고기의 수, 사전 순서
    for idx in range(64):
        count = 0 # 제외되는 물고기의 수
        now = candi[idx]
        arr = []
        x, y = sx, sy
        for d in now:
            x = x + sdx[d]
            y = y + sdy[d]

            if 0 <= x < 4 and 0 <= y < 4:
                if graph[x][y] and (x, y) not in arr:
                    count += len(graph[x][y])
                    arr.append((x, y))
            else:
                break
        else:
            if move[0] < count:
                move = [count, idx]

    now = move[1]
    for d in candi[now]:
        sx = sx + sdx[d]
        sy = sy + sdy[d]
        if graph[sx][sy]:
            graph[sx][sy] = []
            smell[sx][sy] = 3

def smell_spread():
    for x in range(4):
        for y in range(4):
            if smell[x][y] > 0:
                smell[x][y] -= 1

def add_fish():
    for x in range(4):
        for y in range(4):
            if copy_graph[x][y]:
                if graph[x][y]:
                    graph[x][y].extend(copy_graph[x][y])
                else:
                    graph[x][y] = copy_graph[x][y]

for _ in range(s):
    copy_graph = [i[:] for i in graph]
    fish_move()
    shark_move()
    smell_spread()
    add_fish()

result = 0
for x in range(4):
    for y in range(4):
        if graph[x][y]:
            result += len(graph[x][y])

print(result)