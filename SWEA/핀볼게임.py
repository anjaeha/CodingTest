dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move(sx, sy, d):
    x, y = sx, sy
    count = 0

    while 1:
        nx = x + dx[d]
        ny = y + dy[d]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            return (count * 2 + 1)

        if graph[nx][ny] == -1 or (nx == sx and ny == sy):
            return count

        if graph[nx][ny] == 0:
            x, y = nx, ny
            continue
        elif graph[nx][ny] == 1:
            count += 1
            if d == 1:
                d = 3
            elif d == 2:
                d = 0
            else:
                d ^= 1
        elif graph[nx][ny] == 2:
            count += 1
            if d == 0:
                d = 3
            elif d == 2:
                d = 1
            else:
                d ^= 1
        elif graph[nx][ny] == 3:
            count += 1
            if d == 0:
                d = 2
            elif d == 3:
                d = 1
            else:
                d ^= 1
        elif graph[nx][ny] == 4:
            count += 1
            if d == 1:
                d = 2
            elif d == 3:
                d = 0
            else:
                d ^= 1
        elif graph[nx][ny] == 5:
            count += 1
            d ^= 1
        elif 6 <= graph[nx][ny] <= 10:
            for rc in holl[graph[nx][ny]]:
                if nx == rc[0] and ny == rc[1]:
                    continue
                nx = rc[0]
                ny = rc[1]
                break

        x, y = nx, ny

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    holl = {}
    zeros = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                zeros.append((i, j))
            elif 6 <= graph[i][j] <= 10:
                if holl.get(graph[i][j]) is None:
                    holl[graph[i][j]] = [(i, j)]
                else:
                    holl[graph[i][j]].append((i, j))

    result = 0
    for x, y in zeros:
        for d in range(4):
            temp = move(x, y, d)
            result = max(result, temp)


    print("#%d %d" %(tc, result))