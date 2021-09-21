from copy import deepcopy

# 물고기의 위치 찾기
def find_fish(idx):
    for i in range(4):
        for j in range(4):
            if graph[i][j][0] == idx:
                return (i, j)
    return False

# 작은 물고기부터 움직이기 시작
def fish_move(shark_x, shark_y):
    for idx in range(1, 17):
        position = find_fish(idx)
        if position == False:
            continue
        x, y = position[0], position[1]
        for _ in range(8):
            d = graph[x][y][1]
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < 4 and 0 <= ny < 4:
                if not (nx == shark_x and ny == shark_y):
                    graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]
                    break
            graph[x][y][1] = (graph[x][y][1] + 1) % 8

# 상어가 갈 수 있는 위치 찾기
def shark_food(x, y):
    food = []
    d = graph[x][y][1]
    for i in range(1, 4):
        nx = x + dx[d] * i
        ny = y + dy[d] * i

        if 0 <= nx < 4 and 0 <= ny < 4 and 1 <= graph[nx][ny][0] <= 16:
            food.append((nx, ny))
    return food


shark = 0
def dfs(x, y, total):
    global shark, graph

    number = graph[x][y][0]
    graph[x][y][0] = -1 # 상어가 먹음
    
    fish_move(x, y)
    food = shark_food(x, y)

    shark = max(shark, total + number)

    for nx, ny in food:
        temp = deepcopy(graph)
        dfs(nx, ny, total + number)
        graph = deepcopy(temp)



dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

graph = [[0] * 4 for _ in range(4)]

for i in range(4):
    a, a1, b, b1, c, c1, d, d1 = map(int, input().split())
    graph[i][0] = [a, a1 - 1]
    graph[i][1] = [b, b1 - 1]
    graph[i][2] = [c, c1 - 1]
    graph[i][3] = [d, d1 - 1]

dfs(0, 0, 0)
print(shark)