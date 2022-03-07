from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]

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

def move(x, y, d):
    cnt = 0
    while graph[x + dx[d]][y + dy[d]] != '#' and graph[x][y] != 'O':
        x = x + dx[d]
        y = y + dy[d]
        cnt += 1
    return x, y, cnt

def bfs():
    while q:
        rx, ry, bx, by, cnt = q.popleft()

        for d in range(4): # 기울이기
            rnx, rny, rcnt = move(rx, ry, d)
            bnx, bny, bcnt = move(bx, by, d)

            if graph[bnx][bny] != 'O': # 파란색이 빠져나오면 게임 종료
                if graph[rnx][rny] == 'O': # 빨간색이 나오면 횟수 출력
                    print(cnt)
                    return

                if (rnx, rny) == (bnx, bny):
                    if rcnt < bcnt:
                        bnx = bnx - dx[d]
                        bny = bny - dy[d]
                    else:
                        rnx = rnx - dx[d]
                        rny = rny - dy[d]

                if not visit[rnx][rny][bnx][bny]:
                    visit[rnx][rny][bnx][bny] = True
                    if cnt < 10:
                        q.append((rnx, rny, bnx, bny, cnt + 1))
    print(-1)

bfs()