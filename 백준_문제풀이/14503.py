import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
x, y, d = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]


def clean(x, y, d):
    global answer

    if s[x][y] == 0:
        answer += 1
        s[x][y] = 2

    for i in range(4):
        nd = (d + 3) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]

        if s[nx][ny] == 0:
            clean(nx, ny, nd)
            return
        d = nd

    nd = (d + 2) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]

    if s[nx][ny] == 1:
        return


    clean(nx, ny, d)

answer = 0
clean(x, y, d)
print(answer)