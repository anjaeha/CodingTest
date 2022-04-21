from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

virus_pos = []
zero_pos = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            zero_pos.append((i, j))
        elif graph[i][j] == 2:
            virus_pos.append((i, j))

candi = []
temp = []
visit = [False] * len(zero_pos)
def make_candi(depth):
    if depth == 3:
        candi.append(list(temp))
        return

    for i in range(len(zero_pos)):
        if visit[i]:
            continue
        visit[i] = True
        temp.append(zero_pos[i])
        make_candi(depth + 1)
        temp.pop()
        for j in range(i + 1, len(zero_pos)):
            visit[j] = False

def virus():
    q = deque()
    for x, y in virus_pos:
        q.append((x, y))

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 2
                    q.append((nx, ny))

def check():
    global result
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                cnt += 1
    result = max(result, cnt)

def make_wall(arr):
    for x, y in arr:
        graph[x][y] = 1

make_candi(0)
board = [i[:] for i in graph]
result = -1
for idx in range(len(candi)):
    graph = [i[:] for i in board]
    now = candi[idx]
    make_wall(now)
    virus()
    check()

print(result)