# 위치(r, c) 질량M 방향D 속력S
# 행과 열은 1부터 N까지 있음
# 1번행은 N번행과 연결, 1번열은 N번열과 연결
# 1. 모든 파이벌이 방향d로 속력S칸만큼 이동 (이동하는 중에는 같은 칸에 여러 파이어볼이 있을 수 있음)
# 2. 이동이 끝나고, 2개 이상이 잇으면,
# 2 - 1) 파이어볼이 합쳐짐
# 2 - 2) 파이어볼이 4개로 나눠짐
# 2 - 3) 질량은 합쳐진 질량 / 5, 속력은 속력의 합 / 합쳐진 개수, 방향은 모두 짝수 or 홀수면 0 2 4 6 아니면 1 3 5 7
# 2-  4) 질량이 0이 되면 사라짐
# K번을 이동하고 남아있는 질량의 합

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

""" 딕셔너리를 사용해서 문제를 해결하는 방법
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


n, m, k = map(int, input().split()) # N * N크기의 파이어볼 M개, 이동횟수 K

fireball = {}
for _ in range(m):
    x, y, w, s, d = map(int, input().split()) # 위치(x, y) 무게 속도 방향
    fireball[(x - 1, y - 1)] = [[w, s, d]]

def move_fireball():
    global fireball
    new_ball = {}
    for rc, value in fireball.items():
        for c in range(len(value)):
            val = value[c]

            x, y, w, s, d = rc[0], rc[1], val[0], val[1], val[2]
            nx = (x + (dx[d] * s)) % n
            ny = (y + (dy[d] * s)) % n

            if new_ball.get((nx, ny)) is None:
                new_ball[(nx, ny)] = [[w, s, d]]
            else:
                new_ball[(nx, ny)].append([w, s, d])
    fireball = new_ball

def combine_fireball():
    global fireball
    new_ball = {}

    for rc, val in fireball.items():
        if len(val) == 1:
            new_ball[(rc[0], rc[1])] = [[val[0][0], val[0][1], val[0][2]]]
            continue
        x, y = rc[0], rc[1]
        sum_w = 0
        sum_d = 0
        sum_s = 0

        for w, s, d in val:
            sum_w += w
            sum_s += s
            sum_d += d % 2
        div_w = sum_w // 5
        div_s = sum_s // len(val)


        if div_w == 0:
            continue

        if sum_d == 0 or sum_d == len(val):
            for i in range(4):
                if new_ball.get((x, y)) is None:
                    new_ball[(x, y)] = [[div_w, div_s, i * 2]]
                else:
                    new_ball[(x, y)].append([div_w, div_s, i * 2])
        else:
            for i in range(4):
                if new_ball.get((x, y)) is None:
                    new_ball[(x, y)] = [[div_w, div_s, i * 2 + 1]]
                else:
                    new_ball[(x, y)].append([div_w, div_s, i * 2 + 1])

    fireball = new_ball

for _ in range(k):
    move_fireball()
    combine_fireball()

result = 0
for rc, val in fireball.items():
    for w, s, d in val:
        result += w

print(result)
"""