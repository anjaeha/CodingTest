# 4 * 4 그래프에서 움직임
# M마리의 물고기와 상어, 8방향중 하나로 움직임, 한 칸에 여러마리가 있을 수 있다.
# 상어가 모든 물고기 복제, -> 마지막에 복제되어 칸에 나타남
# 모든 물고기가 한칸 이동, 상어나 물고기냄새가 있는 칸 제외, 못가면 45도 반시계방향 회전, 없으면 이동안함
# 상어가 3칸 이동, 상하좌우로 이동 가능, 물고기 있는 칸으로 가면, 물고기는 죽음 -> 죽으면서 냄새 남긴다. -> 가장 많은 물고기가 죽은 칸으로 이동
# 냄새가 사라짐 (2번 전에 났던 냄새들 삭제)
# 복제완료, 위치와 방향을 그대로 가져옴

# 물고기의 이동 방향
fdx = [0, -1, -1, -1, 0, 1, 1, 1] # 감소할수록 반시계
fdy = [-1, -1, 0, 1, 1, 1, 0, -1]

# 상어의 이동 방향
sdx = [-1, 0, 1, 0]
sdy = [0, -1, 0, 1]

m, n = map(int, input().split()) # 물고기의 수 M, 상어가 마법을 연습한 횟수 N
graph = [[0] * 4 for _ in range(4)] # 4 * 4 그래프에서 움직임
for _ in range(m): # M개의 물고기 정보
    x, y, d = map(int, input().split()) # 물고기의 위치 (x, y) 방향 d
    if graph[x - 1][y - 1]:
        graph[x - 1][y - 1].append(d - 1)
    else:
        graph[x - 1][y - 1] = [d - 1]
sx, sy = map(int, input().split()) # 상어의 위치
sx, sy = sx - 1, sy - 1
smell = [[0] * 4 for _ in range(4)]

def fish_move():
    global graph
    new_graph = [[0] * 4 for _ in range(4)]
    for x in range(4):
        for y in range(4):
            if graph[x][y]: # 0이 아닌 물고기 배열이 존재한다면
                for d in graph[x][y]:
                    for i in range(8):
                        nx = x + fdx[(d - i) % 8]
                        ny = y + fdy[(d - i) % 8]
                        if 0 <= nx < 4 and 0 <= ny < 4 and smell[nx][ny] == 0 and (nx, ny) != (sx, sy): # 격자를 벗어나지 않고, 냄새가 안나고, 상어의 위치와 다름
                            if new_graph[nx][ny]:
                                new_graph[nx][ny].append((d - i) % 8)
                            else:
                                new_graph[nx][ny] = [(d - i) % 8]
                            break
                    else: # 움직일 곳이 없으면
                        if new_graph[x][y]:
                            new_graph[x][y].append(d)
                        else:
                            new_graph[x][y] = [d]
    graph = new_graph

candi = []
temp = []
def make_candi(depth): # 상어가 갈 수 있는 모든 경우의 수를 미리 구해놓는다. 최대 64개라서 오래걸리지 않음
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
    shark_candi = [] # 상어가 갈 수 있는 곳
    for idx in range(len(candi)):
        cnt = 0 # 상어가 먹은 물고기의 수
        arr = []
        x, y = sx, sy
        visit = [[False] * 4 for _ in range(4)]
        for d in range(3):
            sd = candi[idx][d]
            nx = x + sdx[sd]
            ny = y + sdy[sd]
            arr.append(sd)
            if 0 <= nx < 4 and 0 <= ny < 4:
                if graph[nx][ny]:
                    if not visit[nx][ny]:
                        cnt += len(graph[nx][ny])
                        visit[nx][ny] = True
                    else:
                        pass
                x, y = nx, ny
            else:
                break
        else:
            arr.append(cnt)
            shark_candi.append(arr)
    shark_candi.sort(key = lambda x : (-x[3], x[0], x[1], x[2])) # 가장 많이 먹은 순, 사전 순서대로 정렬을 해준다.

    temp = shark_candi[0] # 정렬을 했을때 가장 첫번째값으로 움직이기 시작함
    for i in range(3):
        d = temp[i]
        sx = sx + sdx[d]
        sy = sy + sdy[d]

        if graph[sx][sy]:
            smell[sx][sy] = 3 # 잡아먹은 곳 냄새 3로
            graph[sx][sy] = 0 # 물고기 전부 제외

def smell_spread():
    for x in range(4):
        for y in range(4):
            if smell[x][y]:
                smell[x][y] -= 1

def add_copyfish():
    for x in range(4):
        for y in range(4):
            if temp_graph[x][y]:
                if graph[x][y]:
                    graph[x][y].extend(temp_graph[x][y])
                else:
                    graph[x][y] = temp_graph[x][y]

for _ in range(n):
    temp_graph = [i[:] for i in graph] # 복제 마법 시전
    fish_move() # 물고기 한칸 이동
    shark_move() # 상어 이동
    smell_spread() # 냄새 1빠짐
    add_copyfish()

result = 0
for x in range(4):
    for y in range(4):
        if graph[x][y]:
            result += len(graph[x][y])

print(result)