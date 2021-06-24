import sys, copy
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())

s = [list(map(int, input().split())) for _ in range(n)]

def melt(x, y):
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx > n or ny > m:
            continue

        if t[nx][ny] == 0:
            cnt += 1

    return cnt

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visit = [[0] * m for _ in range(n)]
    visit[x][y] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if temp[nx][ny] != 0 and visit[nx][ny] == 0:
                q.append((nx, ny))
                visit[nx][ny] = 1
                temp[nx][ny] = 0
    
def check():
    for i in range(n):
        for j in range(m):
            if s[i][j] != 0:
                return False
    return True

result = 1
while 1:
    if check():
        print(0)
        break

    t = copy.deepcopy(s)
    for i in range(n):
        for j in range(m):
            if t[i][j] != 0:
                temp = s[i][j] - melt(i, j)
                s[i][j] = temp if temp >= 0 else 0
    temp = copy.deepcopy(s)
    cnt = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] != 0:
                temp[i][j] = 0
                bfs(i, j)
                cnt += 1

    if cnt > 1:
        print(result)
        break

    result += 1