from copy import deepcopy

def find_number(idx):  # 해당 번호의 위치 찾기
    for i in range(4):
        for j in range(4):
            if graph[i][j][0] == idx:
                return i, j
    return False

def fish_move(sx, sy):
    for idx in range(1, 17):
        pos = find_number(idx)
        if not pos:
            continue
        x, y = pos
        for i in range(8):
            d = graph[x][y][1]
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < 4 and 0 <= ny < 4 and (nx, ny) != (sx, sy):
                graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]
                break
            graph[x][y][1] = (graph[x][y][1] + 1) % 8

def shark_food(x, y):
    food = []
    d = graph[x][y][1]
    for i in range(1, 4):
        nx = x + dx[d] * i
        ny = y + dy[d] * i

        if 0 <= nx < 4 and 0 <= ny < 4 and graph[nx][ny][0] > 0:
            food.append((nx, ny))
    return food

result = 0
def dfs(x, y, total):
    global result, graph

    number = graph[x][y][0]
    graph[x][y][0] = -1  # 상어가 먹음

    fish_move(x, y)
    food = shark_food(x, y)

    result = max(result, total + number)

    for nx, ny in food:
        temp = deepcopy(graph)
        dfs(nx, ny, total + number)
        graph = deepcopy(temp)

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

graph = [[0] * 4 for _ in range(4)]

for i in range(4):
    n1, d1, n2, d2, n3, d3, n4, d4 = map(int, input().split())
    graph[i][0] = [n1, d1 - 1]
    graph[i][1] = [n2, d2 - 1]
    graph[i][2] = [n3, d3 - 1]
    graph[i][3] = [n4, d4 - 1]

dfs(0, 0, 0)
print(result)