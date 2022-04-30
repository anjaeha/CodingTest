m, s = map(int, input().split()) # 1 <= 물고기의수 <= 10, 1 <= 마법을 연습한 횟수 <= 100
graph = [[[0] * 8 for _ in range(4)] for _ in range(4)]
for _ in range(m):
    x, y, d = map(int, input().split()) # 좌표와 방향
    graph[x - 1][y - 1][d - 1] += 1

sx, sy = map(int, input().split()) # 상어의 초기 위치
sx, sy = sx - 1, sy - 1

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

sdx = [-1, 0, 1, 0]
sdy = [0, -1, 0, 1]

candi = []
temp = []

def make_candi(depth):
    if depth == 3:
        candi.append(list(temp))
        return

    for i in range(4):
        temp.append(i)
        make_candi(depth + 1)
        temp.pop()
make_candi(0)

def fish_move():
    global graph
    temp_graph = [[[0] * 8 for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            for d in range(8): # 물고기 이동
                if graph[x][y][d]: # 물고기가 있으면
                    for sd in range(8): # 어느 방향으로 이동할지 결정
                        nx = x + dx[(d - sd) % 8]
                        ny = y + dy[(d - sd) % 8]
                        if 0 <= nx < 4 and 0 <= ny < 4 and smell[nx][ny] == 0 and (nx, ny) != (sx, sy): # 범위를 안벗어나고, 상어가 없고, 물고기 냄새가 없을때만 이동
                            temp_graph[nx][ny][(d - sd) % 8] += graph[x][y][d]
                            break
                    else: # 물고기가 이동할 방향이 없으면
                        temp_graph[x][y][d] += graph[x][y][d]
    graph = temp_graph

def shark_move(x, y):
    global sx, sy
    candi_arr = []
    for idx in range(len(candi)):
        now = candi[idx]
        arr = []
        cnt = 0
        tx, ty = x, y
        for d in range(3):
            nx = tx + sdx[now[d]]
            ny = ty + sdy[now[d]]

            if 0 <= nx < 4 and 0 <= ny < 4:
                if (nx, ny) not in arr:
                    cnt += sum(graph[nx][ny])
                    arr.append((nx, ny))
                tx, ty = nx, ny
            else:
                break
        else:
            candi_arr.append((cnt, idx))
    candi_arr.sort(key = lambda x : (-x[0], x[1]))
    move = candi_arr[0]
    now = candi[move[1]]
    for i in range(3):
        x = x + sdx[now[i]]
        y = y + sdy[now[i]]
        for c in range(8):
            if graph[x][y][c]:
                smell[x][y] = 3
                graph[x][y][c] = 0
    sx, sy = x, y

smell = [[0] * 4 for _ in range(4)]
for case in range(s):
    copy_graph = [i[:] for i in graph] # 복제마법
    fish_move() # 물고기 이동 시작
    shark_move(sx, sy) # 상어가 3칸 이동
    for x in range(4):
        for y in range(4):
            if smell[x][y]:
                smell[x][y] -= 1

    for x in range(4):
        for y in range(4):
            for d in range(8):
                if copy_graph[x][y][d]:
                    graph[x][y][d] += copy_graph[x][y][d]

result = 0
for x in range(4):
    for y in range(4):
        result += sum(graph[x][y])

print(result)