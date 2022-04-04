n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dir = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0, 0]
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

def move(d):
    global dice, graph, x, y
    nx = x + dx[d]
    ny = y + dy[d]

    if nx < 0 or ny < 0 or nx >= n or ny >= m: # 범위를 벗어나면 무시
        return

    if d == 1: # 동쪽으로
        dice = [0, dice[4], dice[2], dice[1], dice[6], dice[5], dice[3]]
    elif d == 2: # 서쪽으로
        dice = [0, dice[3], dice[2], dice[6], dice[1], dice[5], dice[4]]
    elif d == 3: # 북쪽으로
        dice = [0, dice[5], dice[1], dice[3], dice[4], dice[6], dice[2]]
    elif d == 4: # 남쪽으로
        dice = [0, dice[2], dice[6], dice[3], dice[4], dice[1], dice[5]]

    if graph[nx][ny] == 0: # 이동한 칸이 0이면
        graph[nx][ny] = dice[6] # 주사위 밑면을 복사
    else:
        dice[6] = graph[nx][ny] # 밑면에 값을 넣고
        graph[nx][ny] = 0 # 0으로 변경
    print(dice[1]) # 주사위의 윗면을 출력
    x, y = nx, ny

for d in dir:
    move(d)