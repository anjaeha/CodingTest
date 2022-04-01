from collections import deque

n = int(input())
k = int(input())
graph = [[0] * n for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = 'A'  # 사과의 위치

l = int(input())
move_dir = [list(input().split()) for _ in range(l)]

dx = [0, 1, 0, -1]  # 우, 하, 좌, 상 => 시계방향
dy = [1, 0, -1, 0]

snack = deque()
snack.append((0, 0))
sd = 0

count = 0
pos = 0
while 1:
    if int(move_dir[pos][0]) == count:
        if move_dir[pos][1] == 'D':
            sd = (sd + 1) % 4
        else:
            sd = (sd - 1) % 4
        if pos == l - 1:
            pass
        else:
            pos += 1

    sx, sy = snack[-1][0], snack[-1][1]

    nx = sx + dx[sd]
    ny = sy + dy[sd]

    if 0 <= nx < n and 0 <= ny < n:
        if (nx, ny) not in snack:
            snack.append((nx, ny))
            if graph[nx][ny] != 'A':  # 사과를 먹지 않으면 크기가 줄어든다
                snack.popleft()
            else:
                graph[nx][ny] = 0
        else:
            break
    else:
        break
    count += 1

print(count + 1)