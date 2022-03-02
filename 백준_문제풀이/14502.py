from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)] # 0 - 빈칸, 1 - 벽, 2 - 바이러스

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] # 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나간다.

zero_pos = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            zero_pos.append((i, j)) # 0의 위치 탐색 -> 벽을 세울수 있는 공간

candi = []
temp = []
visit = [False] * len(zero_pos)
def make_candi(cnt): # 만들 수 있는 모든 조합을 구하는 함수
    if cnt == 3:
        candi.append(list(temp))
        return

    for i in range(len(zero_pos)):
        if visit[i]:
            continue

        visit[i] = True
        temp.append(zero_pos[i])
        make_candi(cnt + 1)
        temp.pop()
        for j in range(i + 1, len(zero_pos)):
            visit[j] = False
make_candi(0)

def spread(board): # 바이러스 퍼지는 함수
    q = deque()
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 0:
                    board[nx][ny] = 2
                    q.append((nx, ny))

MAX = -1
for i in range(len(candi)):
    board = [item[:] for item in graph]
    for x, y in candi[i]:
        board[x][y] = 1

    spread(board)
    cnt = 0
    for i in range(n): # 안전구역 구하기
        for j in range(m):
            if board[i][j] == 0:
                cnt += 1

    MAX = max(MAX, cnt)

print(MAX)