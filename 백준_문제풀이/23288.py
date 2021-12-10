from collections import deque

n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
game_board = [[0] * m for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# 동, 남, 서, 북

def search_grade(): # 점수 얻는 판 미리 구해놓기
    for i in range(n):
        for j in range(m):
            visit = [[False] * m for _ in range(n)]
            q = deque()
            cnt = 1
            start = board[i][j]
            visit[i][j] = True
            q.append((i, j))

            while q:
                x, y = q.popleft()
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if 0 <= nx < n and 0 <= ny < m:
                        if start == board[nx][ny] and not visit[nx][ny]:
                            visit[nx][ny] = True
                            q.append((nx, ny))
                            cnt += 1
            game_board[i][j] = board[i][j] * cnt
search_grade()

# 윗1, 뒤2, 오3 왼4, 앞5 밑6
dice = [1, 2, 3, 4, 5, 6]

def dice_move(dir):
    global dice
    if dir == 0: # 주사위 오른쪽으로 굴리면
        new_dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    elif dir == 2: #주사위 왼쪽으로 굴리면
        new_dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    elif dir == 1: #주사위 앞으로 굴리면
        new_dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]
    elif dir == 3: #주사위 뒤로 굴리면
        new_dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
    dice = new_dice

def compare_score(A, B): # 주사위의 아랫면A, 주사위가 있는칸 B
    global sd
    if A > B:
        sd = (sd + 1) % 4
    elif A < B:
        sd = (sd - 1) % 4
    
sx, sy, sd = 0, 0, 0
# 시작위치 (0, 0) 방향 동쪽
score = 0


for case in range(k):
    tx = sx + dx[sd]
    ty = sy + dy[sd]

    if 0 <= tx < n and 0 <= ty < m:
        sx, sy = tx, ty
    else:
        sd = (sd + 2) % 4
        sx = sx + dx[sd]
        sy = sy + dy[sd]
    
    dice_move(sd)
    compare_score(dice[5], board[sx][sy])
    score += game_board[sx][sy]

print(score)