# 낚시왕 이동, 상어잡고, 상어 이동 순서
# 벽에 부딪히면 방향 반대로
# 상어가 두마리 이상이면, 큰 상어가 잡아먹음

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def fishing(y):
    global result
    for i in range(n):
        if graph[i][y] != 0:
            result += graph[i][y][2]
            graph[i][y] = 0
            return

def move_shark():
    global graph
    temp = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                cur = graph[i][j]
                s, d, z = cur[0], cur[1], cur[2] # 속도 방향 크기
                x, y = i, j
                if d == 0 or d == 1: # 위 혹은 아래
                    s = s % (n + n - 2)
                elif d == 2 or d == 3:
                    s = s % (m + m - 2)
                for c in range(s):
                    x = x + dx[d]
                    y = y + dy[d]

                    if d == 0 or d == 1:
                        if x >= n - 1 or x <= 0:
                            if x > n - 1:
                                x = n - 2
                            elif x < 0:
                                x = 1
                            d ^= 1
                    elif d == 2 or d == 3:
                        if y >= m - 1 or y <= 0:
                            if y > m - 1:
                                y = m - 2
                            elif y < 0:
                                y = 1
                            d ^= 1

                if temp[x][y] == 0:
                    temp[x][y] = [s, d, z]
                else:
                    if temp[x][y][2] > z:
                        continue
                    else:
                        temp[x][y] = [s, d, z]
    graph = [item[:] for item in temp]


n, m, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]

for _ in range(k):
    x, y, s, d, z = map(int, input().split())
    # 좌표와, 속도, 방향, 크기
    graph[x - 1][y - 1] = [s, d - 1, z]
result = 0

for i in range(m):
    fishing(i)
    move_shark()

print(result)