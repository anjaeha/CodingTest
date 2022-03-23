dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

n, m, k = map(int, input().split())
graph = [[0] * n for _ in range(n)]

for i in range(m):
    x, y, w, s, d = map(int, input().split()) # (x, y)에 질량w, 속도 s, 방향d
    graph[x - 1][y - 1] = [[w, s, d]]

def ball_move():
    global graph
    board = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                continue
            for c in range(len(graph[i][j])):
                w, s, d = graph[i][j][c] # 질량 속도 방향
                nx = (i + dx[d] * s) % n
                ny = (j + dy[d] * s) % n
                if board[nx][ny] == 0:
                    board[nx][ny] = [[w, s, d]]
                else:
                    board[nx][ny].append((w, s, d))

    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                continue
            if len(board[i][j]) <= 1:
                continue
            sum_w = 0 # 질량의 합
            sum_s = 0 # 속력의 합
            sum_i = 0 # 합쳐진 개수
            sum_d = 0 # 방향
            for c in range(len(board[i][j])):
                w, s, d = board[i][j][c]  # 질량 속도 방향
                sum_w += w
                sum_s += s
                sum_i += 1
                sum_d += d % 2

            board[i][j] = []
            cnt_w = sum_w // 5 # 나누어진 파이어볼의 질량
            cnt_s = sum_s // sum_i # 나누어진 파이어볼의 속력
            if cnt_w == 0:
                continue
            if sum_d == sum_i or sum_d == 0: # 모두 짝수이거나 홀수이면
                for idx in range(4):
                    board[i][j].append((cnt_w, cnt_s, idx * 2))
            else:
                for idx in range(4):
                    board[i][j].append((cnt_w, cnt_s, idx * 2 + 1))
    graph = board


for _ in range(k):
    ball_move()

result = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            continue
        for c in range(len(graph[i][j])):
            result += graph[i][j][c][0]

print(result)