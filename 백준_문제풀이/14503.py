import sys
input = sys.stdin.readline
n, m = map(int, input().split())

x, y, d = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

s[x][y] = 2
count = 1

while 1:
    check = False

    for i in range(4):
        d = (d - 1) % 4
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < m:
            if s[nx][ny] == 0:
                s[nx][ny] = 2
                x, y = nx, ny
                count += 1
                check = True
                break
                
    if not check:
        nx = x - dx[d]
        ny = y - dy[d]

        if 0 <= nx < n and 0 <= ny < m:
            if s[nx][ny] == 2:
                x, y = nx, ny
            elif s[nx][ny] == 1:
                print(count)
                break
        else:
            print(count)
            break