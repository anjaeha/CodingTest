from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def big_block():
    global result
    arr = []
    visit = [[False] * n for _ in range(n)]
    for rx in range(n):
        for ry in range(n):
            if not visit[rx][ry] and graph[rx][ry] > 0:
                now = graph[rx][ry]
                visit[rx][ry] = True
                q = deque()
                q.append((rx, ry))
                rainbow = []
                color = [(rx, ry)]
                while q:
                    x, y = q.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]

                        if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
                            if graph[nx][ny] == now: # 무지개색이거나 같은 색
                                visit[nx][ny] = True
                                color.append((nx, ny))
                                q.append((nx, ny))
                            elif graph[nx][ny] == 0:
                                rainbow.append((nx, ny))
                                q.append((nx, ny))
                                visit[nx][ny] = True
                arr.append((len(color) + len(rainbow), len(rainbow), rx, ry))
                for x, y in rainbow:
                    visit[x][y] = False
    if not arr:
        return False
    arr.sort(key = lambda x : (-x[0], -x[1], -x[2], -x[3]))
    if arr[0][0] < 2:
        return False
    now = arr[0]
    result += now[0] ** 2
    rx, ry = now[2], now[3]
    q = deque()
    q.append((rx, ry))
    now_color = graph[rx][ry]
    graph[rx][ry] = -2
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == now_color or graph[nx][ny] == 0:
                    graph[nx][ny] = -2
                    q.append((nx, ny))
    return True
def gravity():
    for y in range(n):
        for x in range(n - 1, 0, -1):
            if graph[x][y] == -2:
                nx = x
                while nx - 1 > 0 and graph[nx - 1][y] == -2:
                    nx -= 1
                if graph[nx - 1][y] != -1:
                    graph[x][y] = graph[nx - 1][y]
                    graph[nx - 1][y] = -2

def rotate():
    global graph
    new_graph = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            new_graph[x][y] = graph[y][n - 1 - x]
    graph = new_graph

result = 0
while 1:
    temp = big_block()
    if not temp:
        break
    gravity()
    rotate()
    gravity()

print(result)