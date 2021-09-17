n, k = map(int, input().split())
# 0흰, 1빨, 2파
graph = [list(map(int, input().split())) for _ in range(n)]
chess_map = [[[] for _ in range(n)] for _ in range(n)]
chess = [0 for _ in range(k)]
# 체스말 위치
for i in range(k):
    x, y, c = map(int, input().split())
    chess_map[x - 1][y - 1].append(i)
    chess[i] = [x - 1, y - 1, c - 1]
# 오른쪽, 왼쪽, 위, 아래
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def move(number):
    # 현재 체스의 위치와 방향을 불러옴
    x, y, d = chess[number]
    nx = x + dx[d]
    ny = y + dy[d]
    # 가려는 방향이 범위를 벗어나거나 파란색이면 방향 변경
    if nx < 0 or ny < 0 or nx >= n or ny >= n or graph[nx][ny] == 2:
        nd = d ^ 1 # 0을 1로, 1을 0으로, 2를 3, 3을 2로 변경하기
        chess[number][2] = nd
        nx = x + dx[nd]
        ny = y + dy[nd]
        # 가려는 방향의 반대 방향도 범위를 벗어나거나 파란색이면 방향 변경
        if nx < 0 or ny < 0 or nx >= n or ny >= n or graph[nx][ny] == 2:
            return False

    # 위에 올라와 있는 말포함해서 움직이기
    chess_set = []
    for i in range(len(chess_map[x][y])):
        if chess_map[x][y][i] == number:
            chess_set.extend(chess_map[x][y][i:])
            chess_map[x][y] = chess_map[x][y][:i]
            break
    # 가려는 곳의 색이 빨강이면 역순
    if graph[nx][ny] == 1:
        chess_set = chess_set[::-1]
    # 가려는 곳의 좌표로 바꿔주기
    for i in chess_set:
        chess_map[nx][ny].append(i)
        chess[i][:2] = [nx, ny]
    # 턴이 진행되던 중에 말이 4개 이상 쌓이는 순간 게임이 종료 조건 만족하면 끝
    if len(chess_map[nx][ny]) >= 4:
        return True
    return False


# 1000번 이하일때만 정답 출력
idx = 1
while idx <= 1000:
    for i in range(k):
        flag = move(i)
        if flag:
            print(idx)
            exit()
    idx += 1

print(-1)