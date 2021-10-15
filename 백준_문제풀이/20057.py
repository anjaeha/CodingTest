def move(x, y, dir):
    global result

    lost_sand = 0 # 잃어버린 모래양을 파악하기 위한 변수

    for dx, dy, per in dir:
        nx = x + dx
        ny = y + dy

        if per == 0:
            new_sand = graph[x][y] - lost_sand
            graph[x][y] = 0 # y에 있던 모든 모래가 a쪽으로 옮겨지기 때문에 0으로 설정 해줌.
        else:
            new_sand = int(graph[x][y] * per)
            lost_sand += int(graph[x][y] * per)

        if 0 <= nx < n and 0 <= ny < n:
            graph[nx][ny] += new_sand

        else:
            result += new_sand

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]


left = [(0, -2, 0.05), (-1, -1, 0.1), (-1, 0, 0.07), (-2, 0, 0.02), (-1, 1, 0.01), (1, -1, 0.1), (1, 0, 0.07), (2, 0, 0.02), (1, 1, 0.01), (0, -1, 0)]
right = [(x, -y, z) for x, y, z in left]
up = [(y, x, z) for x, y, z, in left]
down = [(-y, x, z) for x, y, z, in left]

dic = {0 : left, 1 : down, 2 : right, 3 : up}

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
# 좌, 하, 우, 상

sx, sy = n // 2, n // 2
d = 0
result = 0

for case in range(2 * n - 1): # 방향 전환 횟수
    if case == 2 * n - 2:
        cnt = case // 2
    else:
        cnt = case // 2 + 1

    for idx in range(cnt):
        nx = sx + dx[d]
        ny = sy + dy[d]
        move(nx, ny, dic[d])
        sx,sy = nx, ny

    d = (d + 1) % 4

print(result)