import sys
input = sys.stdin.readline
from collections import deque

N, L, R = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    temp = []
    temp.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0:
                if L <= abs(s[x][y] - s[nx][ny]) <= R:
                    visit[nx][ny] = 1
                    q.append((nx, ny))
                    temp.append((nx, ny))

    return temp

cnt = 0
while 1:
    flag = False
    visit = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0:
                visit[i][j] = 1
                temp = bfs(i, j)

                if len(temp) > 1:
                    flag = True
                    num = sum(s[x][y] for x, y in temp) // len(temp)
                    for x, y in temp:
                        s[x][y] = num

    if flag == False:
        break
    cnt += 1

print(cnt)