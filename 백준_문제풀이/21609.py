from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_block():
    visit = [[False] * n for _ in range(n)]
    candi = []
    for r in range(n):
        for c in range(n):
            if graph[r][c] == '.':
                continue
            if graph[r][c] > 0:
                q = deque()
                q.append((r, c))
                color_block = [(r, c)]
                visit[r][c] = True
                rainbow_block = []
                now = graph[r][c]
                while q:
                    x, y = q.popleft()

                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]

                        if 0 <= nx < n and 0 <= ny < n:
                            if not visit[nx][ny] and graph[nx][ny] in [now, 0]:
                                visit[nx][ny] = True
                                q.append((nx, ny))
                                if graph[nx][ny] == 0:
                                    rainbow_block.append((nx, ny))
                                elif graph[nx][ny] == now:
                                    color_block.append((nx, ny))
                for x, y in rainbow_block:
                    visit[x][y] = False
                if len(color_block) + len(rainbow_block) >= 2:
                    candi.append((color_block + rainbow_block, len(rainbow_block), r, c))
    candi.sort(key = lambda x : (-len(x[0]), -x[1], -x[2], -x[3]))
    if candi:
        return candi[0] # 블럭, 무지개 블록의 개수, 좌표(r, c)
    else:
        return False

def remove_block(arr):
    global result
    result += len(arr[0]) ** 2
    for x, y in arr[0]:
        graph[x][y] = '.' # 삭제된 블럭

def gravity():
    for y in range(n):
        for x in range(n - 1, 0, -1):
            if graph[x][y] == '.':
                nx = x
                while nx >= 1 and graph[nx][y] == '.':
                    nx -= 1
                if graph[nx][y] != -1:
                    graph[x][y] = graph[nx][y]
                    graph[nx][y] = '.'

def rotate():
    global graph
    board = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            board[x][y] = graph[y][n - x - 1]
    graph = board

result = 0
while 1:
    arr = find_block()
    if not arr:
        break
    remove_block(arr)
    gravity()
    rotate()
    gravity()

print(result)