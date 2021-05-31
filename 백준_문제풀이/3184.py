
sheep = 0
wolf = 0

r, c = map(int, input().split())
s = [list(input().strip()) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    wolf_cnt = 0
    sheep_cnt = 0
    q = [(i, j)]

    while q:
        x, y = q.pop()
        if s[x][y] == 'v':
            wolf_cnt += 1
        if s[x][y] == 'o':
            sheep_cnt += 1
        s[x][y] = '#'

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                if s[nx][ny] != '#':
                    q.append((nx, ny))

    if sheep_cnt <= wolf_cnt:
        sheep_cnt = 0
    else:
        wolf_cnt = 0
    return sheep_cnt, wolf_cnt

for i in range(r):
    for j in range(c):
        if s[i][j] == 'v' or s[i][j] == 'o':
            o, v = bfs(i, j)
            sheep += o
            wolf += v

print(sheep, wolf)