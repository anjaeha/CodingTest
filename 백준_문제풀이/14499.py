# 주사위의 모든 면에는 0이 적혀있다.
# 이동 칸의 수가 0이면, 주사위의 바닥면이 복사
# 0이 아니면, 주사위의 바닥에 복사하고 바닥을 0으로 바꿈

# 동, 서, 북, 남
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

n, m, x, y, k = map(int, input().split()) # 세로N, 가로M, 주사위좌표 X, Y, 명령의 개수 K
graph = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0, 0] # 1이 윗면, 6이 바닥

def move(d): # 주사위 굴리기
    global dice
    if d == 1: # 동쪽으로 굴리기
        dice = [0, dice[4], dice[2], dice[1], dice[6], dice[5], dice[3]]
    elif d == 2: # 서쪽으로 굴리기
        dice = [0, dice[3], dice[2], dice[6], dice[1], dice[5], dice[4]]
    elif d == 3: # 북쪽으로 굴리기
        dice = [0, dice[5], dice[1], dice[3], dice[4], dice[6], dice[2]]
    elif d == 4: # 남쪽으로 굴리기
        dice = [0, dice[2], dice[6], dice[3], dice[4], dice[1], dice[5]]

for i in range(k):
    d = order[i]
    nx, ny = x + dx[d], y + dy[d]
    if 0 <= nx < n and 0 <= ny < m:
        move(d)
        if graph[nx][ny] == 0:
            graph[nx][ny] = dice[6]
        else:
            dice[6] = graph[nx][ny]
            graph[nx][ny] = 0
        x, y = nx, ny
        print(dice[1])