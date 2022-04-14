n, m, k = map(int, input().split())
graph = [[0] * n for _ in range(n)]
for _ in range(m):
    x, y, w, s, d = map(int, input().split())
    graph[x - 1][y - 1] = [[w, s, d]] # 질량 속력 방향

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def move(): # 파이어볼 이동
    global graph
    temp_graph = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if graph[x][y]:
                for idx in range(len(graph[x][y])):
                    now = graph[x][y][idx]
                    nx = (x + dx[now[2]] * now[1]) % n
                    ny = (y + dy[now[2]] * now[1]) % n

                    if temp_graph[nx][ny] == 0:
                        temp_graph[nx][ny] = [now]
                    else:
                        temp_graph[nx][ny].append(now)
    graph = temp_graph

def div_fireball():
    for x in range(n):
        for y in range(n):
            if graph[x][y] and len(graph[x][y]) > 1:
                weight, speed, cnt, dire = 0, 0, 0, 0 # 합쳐진 질량, 속력, 개수, 방향
                for idx in range(len(graph[x][y])):
                    now = graph[x][y][idx]
                    weight += now[0]
                    speed += now[1]
                    dire += now[2] % 2 # 홀수인지 짝수인지만 알면됨
                    cnt += 1
                if weight >= 5:
                    graph[x][y] = []
                    if dire == cnt or dire == 0:
                        for i in range(4):
                           graph[x][y].append([weight // 5, speed // cnt, i * 2])
                    else:
                        for i in range(4):
                            graph[x][y].append([weight // 5, speed // cnt, i * 2 + 1])
                else:
                    graph[x][y] = 0

for i in range(k):
    move()
    div_fireball()


result = 0
for x in range(n):
    for y in range(n):
        if graph[x][y]:
            for i in range(len(graph[x][y])):
                result += graph[x][y][i][0]
print(result)