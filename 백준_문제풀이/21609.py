# 크기가 가장 큰 블록 -> 무지개 블록의 수가 많은 -> 행, 열이 가장 큰
# 중력 작용 -> 반시계회전 -> 중력 작용
# 검은색 -1, 무지개 0,
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def make_candi():
    visit = [[False] * n for _ in range(n)]
    candi = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0 and not visit[i][j]:
                visit[i][j] = True
                q = deque()
                q.append((i, j))
                arr = [(i, j)] # 같은 색상의 블록
                rainbow = [] # 무지개 블록
                while q:
                    x, y = q.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]

                        if 0 <= nx < n and 0 <= ny < n:
                            if not visit[nx][ny] and (graph[nx][ny] == 0 or graph[nx][ny] == graph[i][j]):
                                visit[nx][ny] = True
                                q.append((nx, ny))
                                if graph[nx][ny] == graph[i][j]:
                                    arr.append((i, j))
                                if graph[nx][ny] == 0:
                                    rainbow.append((nx, ny))
                for x, y in rainbow:
                    visit[x][y] = False
                arr.sort(key = lambda x : (x[0], x[1]))
                candi.append((len(arr) + len(rainbow), len(rainbow), arr[0][0], arr[0][1]))

    if candi:
        candi.sort(key = lambda x : (-x[0], -x[1], -x[2], -x[3]))
    else:
        return False

    if candi[0][0] >= 2: # 블록의 개수는 2보다 크거나 같아야 함.
        return candi[0]
    else:
        return False

def boom(arr):
    i, j = arr[2], arr[3]
    q = deque()
    q.append((i, j))
    now = graph[i][j]
    graph[i][j] = -2 # 터진공간을 -2로 처리
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 0 or graph[nx][ny] == now:
                    graph[nx][ny] = -2
                    q.append((nx, ny))


def gravity():
    for y in range(n):
        for x in range(n - 1, -1, -1):
            if graph[x][y] == -2: # 빈 공간이면
                nx, ny = x, y
                while 1:
                    if nx - 1 < 0:
                        break
                    if graph[nx - 1][y] == -2:
                        nx = nx - 1
                    else:
                        nx = nx - 1
                        break
                if graph[nx][ny] == -1:
                    continue
                else:
                    graph[x][y] = graph[nx][ny]
                    graph[nx][ny] = -2

def rotate():
    global graph
    board = [[-3] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            board[i][j] = graph[j][n - i - 1]
    graph = board

result = 0
while 1:
    candi = make_candi()
    if not candi:
        break
    result += candi[0] ** 2
    boom(candi)
    gravity()
    rotate()
    gravity()

print(result)