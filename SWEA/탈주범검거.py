from copy import deepcopy
def move():
    global r, c
    new = deepcopy(pos)
    for rc, val in pos.items():
        i, j = rc[0], rc[1]

    
        if graph[i][j] == 1:
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0 <= nx < n and 0 <= ny < m:
                    if d == 0:
                        if graph[nx][ny] in [1, 2, 5, 6]:
                            new[(nx, ny)] = graph[nx][ny]
                    elif d == 1:
                        if graph[nx][ny] in [1, 2, 4, 7]:
                            new[(nx, ny)] = graph[nx][ny]
                    elif d == 2:
                        if graph[nx][ny] in [1, 3, 4, 5]:
                            new[(nx, ny)] = graph[nx][ny]
                    elif d == 3:
                        if graph[nx][ny] in [1, 3, 6, 7]:
                            new[(nx, ny)] = graph[nx][ny]
        elif graph[i][j] == 2:
            for d in range(2):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0 <= nx < n and 0 <= ny < m:
                    if d == 0:
                        if graph[nx][ny] in [1, 2, 5, 6]:
                            new[(nx, ny)] = graph[nx][ny]
                    elif d == 1:
                        if graph[nx][ny] in [1, 2, 4, 7]:
                            new[(nx, ny)] = graph[nx][ny]
        elif graph[i][j] == 3:
            for d in range(2, 4):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0 <= nx < n and 0 <= ny < m:
                    if d == 2:
                        if graph[nx][ny] in [1, 3, 4, 5]:
                            new[(nx, ny)] = graph[nx][ny]
                    elif d == 3:
                        if graph[nx][ny] in [1, 3, 6, 7]:
                            new[(nx, ny)] = graph[nx][ny]
        elif graph[i][j] == 4:
            for d in range(0, 4, 3):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0 <= nx < n and 0 <= ny < m:
                    if d == 0:
                        if graph[nx][ny] in [1, 2, 5, 6]:
                            new[(nx, ny)] = graph[nx][ny]
                    elif d == 3:
                        if graph[nx][ny] in [1, 3, 6, 7]:
                            new[(nx, ny)] = graph[nx][ny]
        elif graph[i][j] == 5:
            for d in range(1, 4, 2):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0 <= nx < n and 0 <= ny < m:
                    if d == 1:
                        if graph[nx][ny] in [1, 2, 4, 7]:
                            new[(nx, ny)] = graph[nx][ny]
                    elif d == 3:
                        if graph[nx][ny] in [1, 3, 6, 7]:
                            new[(nx, ny)] = graph[nx][ny]
        elif graph[i][j] == 6:
            for d in range(1, 3):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0 <= nx < n and 0 <= ny < m:
                    if d == 1:
                        if graph[nx][ny] in [1, 2, 4, 7]:
                            new[(nx, ny)] = graph[nx][ny]
                    elif d == 2:
                        if graph[nx][ny] in [1, 3, 4, 5]:
                            new[(nx, ny)] = graph[nx][ny]
        elif graph[i][j] == 7:
            for d in range(0, 3, 2):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0 <= nx < n and 0 <= ny < m:
                    if d == 0:
                        if graph[nx][ny] in [1, 2, 5, 6]:
                            new[(nx, ny)] = graph[nx][ny]
                    elif d == 2:
                        if graph[nx][ny] in [1, 3, 4, 5]:
                            new[(nx, ny)] = graph[nx][ny]
    return new

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for case in range(1, T + 1):
    n, m, r, c, l = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    # 0은 빈곳, 1 ~ 7은 터널 구조물 타입
    pos = dict()
    pos[(r, c)] = graph[r][c]
    l -= 1
    while l:
        l -= 1
        pos = move()

    print("#%d %d" %(case, len(pos)))