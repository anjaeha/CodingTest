

n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
direction = list(map(int, input().split()))

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
# 가만히, 동, 서, 북, 남

dice = [0, 0, 0, 0, 0, 0, 0]
# 위, 뒤, 오른, 왼, 앞, 아래

def move(d):
    global dice
    if d == 1: # 동쪽으로 굴리면
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif d == 2: # 서쪽으로 굴리면
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif d == 3: # 북쪽으로 굴리면
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
    elif d == 4: # 남쪽으로 굴리면
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]


for case in range(k):
    dir = direction[case]
    nx = x + dx[dir]
    ny = y + dy[dir]

    if 0 <= nx < n and 0 <= ny < m:
        move(dir)
        if graph[nx][ny] == 0:
            graph[nx][ny] = dice[6]
        else:
            dice[6] = graph[nx][ny]
            graph[nx][ny] = 0
    else:
        continue
    
    x, y = nx, ny
    print(dice[1])