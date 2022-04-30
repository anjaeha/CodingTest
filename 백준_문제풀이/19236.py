from copy import deepcopy

graph = [[0] * 4 for _ in range(4)]
for i in range(4):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    graph[i][0] = [x1, y1 - 1]
    graph[i][1] = [x2, y2 - 1]
    graph[i][2] = [x3, y3 - 1]
    graph[i][3] = [x4, y4 - 1]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def find_fish(idx):
    for x in range(4):
        for y in range(4):
            if graph[x][y][0] == idx:
                return x, y
    return False

def move_fish(sx, sy):
    for idx in range(1, 17):
        temp = find_fish(idx)
        if not temp:
            continue

        x, y = temp
        for d in range(8):
            sd = graph[x][y][1]
            nx = x + dx[sd]
            ny = y + dy[sd]

            if 0 <= nx < 4 and 0 <= ny < 4:
                if (nx, ny) != (sx, sy):
                    graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]
                    break

            graph[x][y][1] = (graph[x][y][1] + 1) % 8

def shark_food(x, y, d):
    food = []
    for i in range(1, 4):
        nx = x + dx[d] * i
        ny = y + dy[d] * i
        if 0 <= nx < 4 and 0 <= ny < 4:
            if graph[nx][ny][0] != -1:
                food.append((nx, ny))
    return food

result = 0
def dfs(sx, sy, count):
    global result, graph
    numbers = graph[sx][sy][0]
    graph[sx][sy][0] = -1

    move_fish(sx, sy)
    result = max(result, count + numbers)
    food = shark_food(sx, sy, graph[sx][sy][1])

    temp_graph = deepcopy(graph)
    for x, y in food:
        dfs(x, y, count + numbers)
        graph = deepcopy(temp_graph)

dfs(0, 0, 0)
print(result)