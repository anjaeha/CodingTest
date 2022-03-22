n, m, k = map(int, input().split()) # N * N크기의 격자, M마리의 상어, K초 후에 냄새 없어짐
graph = [list(map(int, input().split())) for _ in range(n)]
dir = [0] + list(map(int, input().split()))
direction = [[[] for _ in range(5)]] + [[[0]] + [list(map(int, input().split())) for _ in range(4)] for _ in range(m)]

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

shark = {} # 상어 위치 찾기
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            shark[graph[i][j]] = (i, j)
            graph[i][j] = [graph[i][j], k]

def move(): # 상어 이동
    global graph
    board = [i[:] for i in graph]
    for idx in range(1, m + 1):
        temp = shark[idx]
        if temp == (-1, -1):
            continue
        x, y = temp[0], temp[1]
        for d in direction[idx][dir[idx]]:
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 0:
                    if board[nx][ny] == 0:
                        board[nx][ny] = [idx, k]
                        dir[idx] = d
                        shark[idx] = (nx, ny)
                        break
                    else:
                        dir[idx] = -1
                        shark[idx] = (-1, -1)
                        break
        else:
            for d in direction[idx][dir[idx]]:
                nx = x + dx[d]
                ny = y + dy[d]

                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] != 0 and graph[nx][ny][0] == idx:
                        board[nx][ny] = [idx, k]
                        dir[idx] = d
                        shark[idx] = (nx, ny)
                        break
    graph = [i[:] for i in board]

def spread(): # 냄새 빼주기, 0초남았을때도 효과는 남아있음.
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                graph[i][j][1] -= 1

                if graph[i][j][1] == -1:
                    graph[i][j] = 0


def check(): # 상어가 다 빠졌는지 확인하기
    for i in range(2, m + 1):
        if shark[i] != (-1, -1):
            return False
    return True


cnt = 0
while 1:
    cnt += 1
    spread()
    move()
    if check():
        break
    if cnt >= 1000:
        cnt = -1
        break
print(cnt)