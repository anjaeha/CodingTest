from collections import deque

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R':
            rx, ry = i, j
        elif graph[i][j] == 'B':
            bx, by = i, j

visit = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
visit[rx][ry][bx][by] = True
q = deque()
q.append((rx, ry, bx, by, 1))

def ball_move(x, y, d):
    cnt = 0
    while graph[x + dx[d]][y + dy[d]] != '#' and graph[x][y] != 'O':
        x, y = x + dx[d], y + dy[d]
        cnt += 1
    return x, y, cnt


def bfs():
    while q:
        rx, ry, bx, by, cnt = q.popleft()

        for d in range(4):
            nrx, nry, rcnt = ball_move(rx, ry, d)
            nbx, nby, bcnt = ball_move(bx, by, d)

            if graph[nbx][nby] != 'O':
                if graph[nrx][nry] == 'O':
                    print(cnt)
                    return

                if (nrx, nry) == (nbx, nby): # 같은 위치를 차지하면
                    if rcnt < bcnt: # 더 많이 움직인 구슬이 멀리 있는 것
                        nbx -= dx[d]
                        nby -= dy[d]
                    else:
                        nrx -= dx[d]
                        nry -= dy[d]

                if not visit[nrx][nry][nbx][nby]:
                    visit[nrx][nry][nbx][nby] = True
                    if cnt < 10:
                        q.append((nrx, nry, nbx, nby, cnt + 1))

    print(-1)

bfs()