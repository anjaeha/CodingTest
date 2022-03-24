from collections import deque

n, m = map(int, input().split())
N = 2 ** n
graph = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def rotate(size):
    if size == 0:
        return graph
    s = 2 ** size
    board = [[0] * N for _ in range(N)]
    for i in range(0, N, s):
        for j in range(0, N, s):
            for x in range(s):
                for y in range(s):
                    board[i + x][j + y] = graph[i + s - y - 1][j + x]
    return board

def melt():
    global graph
    board = [i[:] for i in graph]
    for x in range(N):
        for y in range(N):
            cnt = 0
            if graph[x][y] > 0:
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < N and 0 <= ny < N:
                        if graph[nx][ny] > 0:
                            cnt += 1
                if cnt < 3:
                    board[x][y] -= 1
    graph = board

MAX = 0
def check(): # 가장 큰 덩어리 칸의 개수 구하기
    global MAX
    visit = [[False] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if not visit[x][y] and graph[x][y] > 0:
                q = deque()
                q.append((x, y))
                visit[x][y] = True
                cnt = 1
                while q:
                    x, y = q.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]

                        if 0 <= nx < N and 0 <= ny < N:
                            if graph[nx][ny] > 0 and not visit[nx][ny]:
                                cnt += 1
                                q.append((nx, ny))
                                visit[nx][ny] = True
                MAX = max(MAX, cnt)

for i in range(m):
    graph = rotate(order[i])
    melt()

SUM = 0
for i in range(N):
    for j in range(N):
        SUM += graph[i][j]

check()
print(SUM)
print(MAX)