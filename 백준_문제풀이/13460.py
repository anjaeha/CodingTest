from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
visit = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

q = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R':
            rx, ry = i, j
        elif graph[i][j] == 'B':
            bx, by = i, j
q.append((rx, ry, bx, by, 1))
visit[rx][ry][bx][by] = True

def move(x, y, d):
    cnt = 0
    while graph[x + dx[d]][y + dy[d]] != '#' and graph[x][y] != 'O':
        x += dx[d]
        y += dy[d]
        cnt += 1

    return x, y, cnt
    

def bfs():
    while q:
        rx, ry, bx, by, idx = q.popleft()
        if idx > 10:
            break

        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, i)
            nbx, nby, bcnt = move(bx, by, i)

            if graph[nbx][nby] != 'O':
                if graph[nrx][nry] == 'O':
                    print(idx)
                    return
                if nrx == nbx and nry == nby:
                    if rcnt > bcnt:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if visit[nrx][nry][nbx][nby] == False:
                    visit[nrx][nry][nbx][nby] = True
                    q.append((nrx, nry, nbx, nby, idx + 1))
    
    print(-1)
bfs()