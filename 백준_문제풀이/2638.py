from collections import deque

def check():
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                return False
    return True

def outside():
    q = deque()
    q.append((0, 0))
    graph[0][0] = 2
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    q.append((nx, ny))
                    graph[nx][ny] = 2  # 외부공기2

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)] # 0빈공간, 1치즈

count = 0
while 1:
    if check():
        print(count)
        break
    count += 1
    board = [i[:] for i in graph]
    outside()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                cnt = 0
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 <= nx < n and 0 <= ny < m:
                        if graph[nx][ny] == 2:
                            cnt += 1
                if cnt >= 2:
                    board[i][j] = 0
    graph = board