# x시간동안 비활성화 상태, x시간이 지나면 활성상태, x시간후 죽음
# 죽더라도 죽은 상태로 해당 위치를 차지함
# 활성화되면 첫 1시간동안 상 하 좌 우로 번식
# 번식된 세포는 비활성화 상태
# 두 개 이상의 줄기세포가 하나의 셀에 번식하려고 하면, 생명력 수치가 높은 줄기세포가 차지함
# 용기의 크기는 무한하다고 가정함
# K시간후, 살아있는 세포 (비활성 + 활성)의 개수를 구하여라

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def breed(sec):
    global  cell
    new_cell = {}
    for rc, val in cell.items():
        new_cell[(rc[0], rc[1])] = [val[0], val[1]]
        if val[1] == -1: # 죽은 것으로 생각
            continue
        if sec - val[1] == val[0] + 1: # 활성화 상태
            x, y = rc[0], rc[1]

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if new_cell.get((nx, ny)) is None:
                    if cell.get((nx, ny)) is None:
                        new_cell[(nx, ny)] = [val[0], sec]
                    else:
                        new_cell[(nx, ny)] = [val[0], val[1]]
                else:
                    if new_cell[(nx, ny)][1] == sec:
                        if new_cell[(nx, ny)][0] < val[0]:
                            new_cell[(nx, ny)] = [val[0], sec]
    cell = new_cell

def dead(sec):
    for rc, val in cell.items():
        if sec - val[1] == val[0] * 2:
            cell[(rc[0], rc[1])][1] = -1

def check():
    cnt = 0
    for rc, val in cell.items():
        if val[1] != -1:
            cnt += 1
    return cnt


T = int(input())

for tc in range(1, T + 1):
    n, m, k = map(int, input().split()) # 세로 N, 가로 M, 시간 K
    graph = [list(map(int, input().split())) for _ in range(n)] # 초기 상태, 0은 빈칸, 1 이상이면 생명력

    cell = {}

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                continue
            cell[(i, j)] = [graph[i][j], 0] # 크기와 시간

    for c in range(1, k + 1):
        breed(c)
        dead(c)

    result = check()

    print("#%d %d" %(tc, result))


""" 배양용기의 최대 크기를 구하고, 생명력 수치를 1 ~ 10을 미리 세팅해놓고 살아있는 세포만 움직이는 방법
T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


for tc in range(1, T + 1):
    n, m, k = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]

    life = [[] for _ in range(11)]
    board = [[0] * (2 * k + m) for _ in range(2 * k + n)]

    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                life[graph[i][j]].append((i + k, j + k))
                board[i + k][j + k] = graph[i][j]

    for time in range(1, k + 1):
        for ver in range(10, 0, -1):
            if time % (ver + 1) != 0:
                continue
            survive = []
            for cur in life[ver]:
                if (k - time) < (ver - 1): # time이 작을때 실행한 세포들은 사라지지만, time이 클 쯤에 실행한 세포들은 살아있는 상태로 끝이나기 때문에, 그것을 고려하여 더해주는 작업임. -> 활성상태
                    survive.append(cur)
                for d in range(4): -> 비활성상태
                    if board[cur[0] + dx[d]][cur[1] + dy[d]] == 0:
                        board[cur[0] + dx[d]][cur[1] + dy[d]] = ver
                        survive.append((cur[0] + dx[d], cur[1] + dy[d]))
            life[ver] = survive

    result = 0
    for i in range(11):
        result += len(life[i])

    print("#%d %d" %(tc, result))
"""