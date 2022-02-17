from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def melt(): # 다 녹았는지를 검사하기 위한 함수
    SUM = 0
    for i in range(n):
        SUM += sum(graph[i])
    return SUM == 0

time = 0
while 1:
    if melt():
        break
    time += 1
    q = deque()
    q.append((0, 0))
    board = [[0] * m for _ in range(n)]
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and board[nx][ny] == 0:
                    board[nx][ny] = 2 # 외부공기는 2로
                    q.append((nx, ny))
                elif graph[nx][ny] == 1 and board[nx][ny] == 0:
                    board[nx][ny] = 1 # 치즈는 1


    for x in range(n):
        for y in range(m):
            if board[x][y] == 1:
                cnt = 0
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < m:
                        if board[nx][ny] == 2:
                            cnt += 1
                if cnt >= 2:
                    graph[x][y] = 0
                else:
                    graph[x][y] = 1
print(time)