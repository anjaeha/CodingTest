from collections import deque
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def caneat(x, y): # 현재위치에서 먹을 수 있는 곳까지의 거리와 좌표 구하기
    global size
    q = deque()
    q.append((x, y, 0))
    visit = [[False] * n for _ in range(n)]
    visit[x][y] = True
    eat = deque()
    while q:
        x, y, cnt = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if not visit[nx][ny]:
                    if size >= graph[nx][ny]:
                        visit[nx][ny] = True
                        q.append((nx, ny, cnt + 1))
                        if size > graph[nx][ny] and graph[nx][ny] != 0:
                            eat.append((nx, ny, cnt + 1))
    eat = sorted(eat, key = lambda x : (x[2], x[0], x[1]))
    return eat

size = 2
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            sharkx, sharky = i, j
            graph[i][j] = 0
eat = 0
result = 0
while 1:
    candi = caneat(sharkx, sharky)
    if candi:
        eatx, eaty, eatdist = candi.pop(0)
        graph[eatx][eaty] = 0
        eat += 1
        sharkx, sharky = eatx, eaty
        result += eatdist

        if eat == size:
            eat = 0
            size += 1
    else:
        break

print(result)