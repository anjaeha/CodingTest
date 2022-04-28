graph = [[0] * 10 for _ in range(10)]

def move_block(size, x, y):
    if size == 1:
        nx, ny = x, y
        while nx + 1 < 10 and graph[nx + 1][ny] == 0:
            nx = nx + 1
        graph[nx][ny] = 1
        nx, ny = x, y
        while ny + 1 < 10 and graph[nx][ny + 1] == 0:
            ny = ny + 1
        graph[nx][ny] = 1

    elif size == 2: # 가로 길이의 블록
        nx, ny = x, y
        while nx + 1 < 10 and graph[nx + 1][ny] == 0 and graph[nx + 1][ny + 1] == 0:
            nx = nx + 1
        graph[nx][ny] = 1
        graph[nx][ny + 1] = 1
        nx, ny = x, y
        while ny + 2 < 10 and graph[nx][ny + 2] == 0:
            ny = ny + 1
        graph[nx][ny] = 1
        graph[nx][ny + 1] = 1

    elif size == 3: # 세로 길이의 블록
        nx, ny = x, y
        while nx + 2 < 10 and graph[nx + 2][ny] == 0:
            nx = nx + 1
        graph[nx][ny] = 1
        graph[nx + 1][ny] = 1
        nx, ny = x, y
        while ny + 1 < 10 and graph[nx][ny + 1] == 0 and graph[nx + 1][ny + 1] == 0:
            ny = ny + 1
        graph[nx][ny] = 1
        graph[nx + 1][ny] = 1

def crush_block():
    global result
    for i in range(6, 10):
        for j in range(4):
            if graph[i][j] == 0:
                break
        else:
            graph.pop(i)
            graph.insert(4, [0] * 10)
            result += 1

    for i in range(4, 6):
        for j in range(4):
            if graph[i][j]:
                graph.pop()
                graph.insert(4, [0] * 10)
                break

    board = [[0] * 10 for _ in range(10)]
    for i in range(10):
        for j in range(10):
            board[i][j] = graph[j][i]

    for i in range(6, 10):
        for j in range(4):
            if board[i][j] == 0:
                break
        else:
            board.pop(i)
            board.insert(4, [0] * 10)
            result += 1

    for i in range(4, 6):
        for j in range(4):
            if board[i][j]:
                board.pop()
                board.insert(4, [0] * 10)
                break

    for i in range(10):
        for j in range(10):
            graph[i][j] = board[j][i]

result = 0
n = int(input())
for i in range(n):
    size, x, y = map(int, input().split())
    move_block(size, x, y)
    crush_block()

cnt = 0
for x in range(6, 10):
    for y in range(4):
        if graph[x][y]:
            cnt += 1

        if graph[y][x]:
            cnt += 1

print(result)
print(cnt)