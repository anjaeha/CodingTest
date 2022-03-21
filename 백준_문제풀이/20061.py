def move(t, x, y):
    if t == 1: # 1 * 1 크기
        for d in range(2):
            nx, ny = x, y
            while 1: # 밑으로 보내기
                if 0 <= nx + dx[d] < 10 and 0 <= ny + dy[d] < 10:
                    if graph[nx + dx[d]][ny + dy[d]] == 0:
                        nx = nx + dx[d]
                        ny = ny + dy[d]
                    else:
                        break
                else:
                    break
            graph[nx][ny] = 1
    elif t == 2:  # 1 * 2 크기의 벽돌
        for d in range(2):
            lx, ly = x, y
            rx, ry = x, y + 1
            while 1:
                if 0 <= lx + dx[d] < 10 and 0 <= ly + dy[d] < 10 and 0 <= rx + dx[d] < 10 and 0 <= ry + dy[d] < 10:
                    if graph[lx + dx[d]][ly + dy[d]] == 0 and graph[rx + dx[d]][ry + dy[d]] == 0:
                        lx, ly = lx + dx[d], ly + dy[d]
                        rx, ry = rx + dx[d], ry + dy[d]
                    else:
                        break
                else:
                    break
            graph[lx][ly] = 1
            graph[rx][ry] = 1
    elif t == 3:  # 2 * 1 크기의 벽돌
        for d in range(2):
            lx, ly = x, y
            rx, ry = x + 1, y
            while 1:
                if 0 <= lx + dx[d] < 10 and 0 <= ly + dy[d] < 10 and 0 <= rx + dx[d] < 10 and 0 <= ry + dy[d] < 10:
                    if graph[lx + dx[d]][ly + dy[d]] == 0 and graph[rx + dx[d]][ry + dy[d]] == 0:
                        lx, ly = lx + dx[d], ly + dy[d]
                        rx, ry = rx + dx[d], ry + dy[d]
                    else:
                        break
                else:
                    break
            graph[lx][ly] = 1
            graph[rx][ry] = 1

def check(): # 4개가 가득 찼는지 확인
    global graph, result
    for i in range(6, 10):
        if graph[i][0] == 1:
            if graph[i][1] == graph[i][2] == graph[i][3] == 1: # 가득 찼으니 점수 올려주고, 빼주고, 5번에 새로운거를 넣어줌
                result += 1
                graph.pop(i)
                graph.insert(4, [0] * 10)
        else:
            continue
    for i in range(4, 6): # 연한 초록색 확인
        for j in range(4):
            if graph[i][j] == 1:
                graph.pop()
                graph.insert(4, [0] * 10)
                break

    board = [[0] * 10 for _ in range(10)]
    for i in range(10):
        for j in range(10):
            board[j][i] = graph[i][j]

    for i in range(6, 10):
        if board[i][0] == 1:
            if board[i][1] == board[i][2] == board[i][3] == 1: # 가득 찼으니 점수 올려주고, 빼주고, 5번에 새로운거를 넣어줌
                result += 1
                board.pop(i)
                board.insert(4, [0] * 10)
        else:
            continue
    for i in range(4, 6): # 연한 초록색 확인
        for j in range(4):
            if board[i][j] == 1:
                board.pop()
                board.insert(4, [0] * 10)
                break
    for i in range(10):
        for j in range(10):
            graph[j][i] = board[i][j]

n = int(input()) # 블록을 놓을 횟수
graph = [[0] * 10 for _ in range(10)]

dx = [1, 0] # 밑으로, 오른쪽으로
dy = [0, 1]

result = 0
for _ in range(n):
    t, x, y = map(int, input().split()) # 블록의 형태 t, 좌표 (x, y)
    move(t, x, y)
    check()

answer = 0
for i in range(10):
    for j in range(10):
        if graph[i][j] == 1:
          answer += 1

print(result)
print(answer)