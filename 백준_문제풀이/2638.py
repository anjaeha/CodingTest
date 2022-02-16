n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check():
    global graph
    board = [[0] * m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if graph[x][y]:
                cnt = 0
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if 0 <= nx < n and 0 <= ny < m:
                        if graph[nx][ny] == 0:
                            cnt += 1
                if cnt >= 2:
                    board[x][y] = 0
                else:
                    board[x][y] = 1

    graph = board

def all_melt():
    SUM = 0
    for i in range(n):
        SUM += sum(graph[i])
    return SUM == 0

time = 0
while 1:
    if all_melt():
        break
    time += 1
    check()
print(time)
# https://www.acmicpc.net/problem/2638