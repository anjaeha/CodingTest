
def move(t, x, y):
    if t == 1:
        nx, ny = x, y
        while nx + 1 < 10 and not graph[nx + 1][ny]:
            nx += 1
        graph[nx][ny] = True
        nx, ny = x, y
        while ny + 1 < 10 and not graph[nx][ny + 1]:
            ny += 1
        graph[nx][ny] = True
    elif t == 2:
        nx, ny = x, y
        while nx + 1 < 10 and not graph[nx + 1][ny] and not graph[nx + 1][ny + 1]:
            nx += 1
        graph[nx][ny] = True
        graph[nx][ny + 1] = True
        nx, ny = x, y
        while ny + 2 < 10 and not graph[nx][ny + 2]:
            ny += 1
        graph[nx][ny] = True
        graph[nx][ny + 1] = True
    elif t == 3:
        nx, ny = x, y
        while nx + 2 < 10 and not graph[nx + 2][ny]:
            nx += 1
        graph[nx][ny] = True
        graph[nx + 1][ny] = True
        nx, ny = x, y
        while ny + 1 < 10 and not graph[nx][ny + 1] and not graph[nx + 1][ny + 1]:
            ny += 1
        graph[nx][ny] = True
        graph[nx + 1][ny] = True

def check():
    global result, graph
    for i in range(6, 10):
        for j in range(4):
            if not graph[i][j]:
                break
        else:
            result += 1
            graph.pop(i)
            graph.insert(4, [False for _ in range(10)])

    for i in range(4, 6):
        for j in range(4):
            if graph[i][j]:
                graph.pop()
                graph.insert(4, [False for _ in range(10)])
                break


    board = [[False] * 10 for _ in range(10)]
    for i in range(10):
        for j in range(10):
            board[i][j] = graph[j][i]

    for i in range(6, 10):
        for j in range(4):
            if not board[i][j]:
                break
        else:
            result += 1
            board.pop(i)
            board.insert(4, [False for _ in range(10)])

    for i in range(4, 6):
        for j in range(4):
            if board[i][j]:
                board.pop()
                board.insert(4, [False for _ in range(10)])
                break
    for i in range(10):
        for j in range(10):
            graph[i][j] = board[j][i]


graph = [[False] * 10 for _ in range(10)]
n = int(input())
result = 0
for _ in range(n): # t, x, y /  1* 1, 1 * 2, 2 * 1
    t, x, y = map(int, input().split())
    move(t, x, y)
    check()

count = 0
for i in range(10):
    for j in range(10):
        if graph[i][j]:
            count += 1

print(result)
print(count)