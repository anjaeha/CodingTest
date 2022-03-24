n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 왼쪽, 아래, 오른쪽, 위
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

dir_left = [(-2, 0, 2), (-1, -1, 10), (-1, 0, 7), (-1, 1, 1), (0, -2, 5), (1, -1, 10), (1, 0, 7), (1, 1, 1), (2, 0, 2), (0, -1, 0)]
dir_down = [(-y, x, c) for x, y, c in dir_left]
dir_right = [(x, -y, c) for x, y, c in dir_left]
dir_up = [(y, -x, c) for x, y, c in dir_left]
dir = {0 : dir_left, 1 : dir_down, 2 : dir_right, 3 : dir_up}

sx, sy, sd = n // 2, n // 2, 0 # 시작 위치와 방향

def move(x, y, d):
    global result
    lost_sand = 0
    for r, c, w in dir[d]:
        nx = x + r
        ny = y + c
        if w == 0: # 이게 항상 마지막
            new_sand = graph[x][y] - lost_sand
            graph[x][y] = 0
        else:
            new_sand = graph[x][y] * w // 100
            lost_sand += graph[x][y] * w // 100

        if 0 <= nx < n and 0 <= ny < n:
            graph[nx][ny] += new_sand
        else:
            result += new_sand


result = 0
for idx in range(2 * n - 1):
    if idx == 2 * n - 2:
        count = idx // 2
    else:
        count = idx // 2 + 1

    for i in range(count):
        sx = sx + dx[sd]
        sy = sy + dy[sd]
        move(sx, sy, sd)
    sd = (sd + 1) % 4

print(result)