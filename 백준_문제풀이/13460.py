from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
visit = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R':
            rx, ry = i, j
        elif graph[i][j] == 'B':
            bx, by = i, j
q = deque()
q.append((rx, ry, bx, by, 1))
visit[rx][ry][bx][by] = True

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
        for d in range(4):
            rnx, rny, rcnt = move(rx, ry, d)
            bnx, bny, bcnt = move(bx, by, d)

            if graph[bnx][bny] != 'O': # 파란색이 나가지 않을때만 진행
                if graph[rnx][rny] == 'O': # 빨간색이 나가면 종료
                    return cnt

                if (rnx, rny) == (bnx, bny): # 만약 좌표가 같으면, 더 움직인것(멀리서온것)을 하나 뒤로 빼줌
                    if rcnt < bcnt: # 파란색이 더 멀리서 옴
                        bnx, bny = bnx - dx[d], bny - dy[d]
                    else:
                        rnx, rny = rnx - dx[d], rny - dy[d]

                if not visit[rnx][rny][bnx][bny]:
                    visit[rnx][rny][bnx][bny] = True
                    if cnt < 10:
                        q.append((rnx, rny, bnx, bny, cnt + 1))
    return -1

answer = bfs()
print(answer)
