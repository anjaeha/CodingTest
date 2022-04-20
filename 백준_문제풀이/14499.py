n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dir = list(map(int, input().split()))

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

dice = [0, 0, 0, 0, 0, 0, 0]
def move_dice(d):
    global dice
    if d == 1: # 동쪽으로
        dice = [0, dice[4], dice[2], dice[1], dice[6], dice[5], dice[3]]
    elif d == 2: # 서쪽으로
        dice = [0, dice[3], dice[2], dice[6], dice[1], dice[5], dice[4]]
    elif d == 3: # 북쪽으로
        dice = [0, dice[5], dice[1], dice[3], dice[4], dice[6], dice[2]]
    elif d == 4: # 남쪽으로
        dice = [0, dice[2], dice[6], dice[3], dice[4], dice[1], dice[5]]

for idx in range(k):
    d = dir[idx]
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < n and 0 <= ny < m:
        move_dice(d)
        if graph[nx][ny] == 0:
            graph[nx][ny] = dice[6]
        else:
            dice[6] = graph[nx][ny]
            graph[nx][ny] = 0
        x, y = nx, ny
        print(dice[1])