from collections import deque
n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    country = [(x, y)]
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if visit[nx][ny] == 0:
                    if l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                        visit[nx][ny] = 1
                        q.append((nx, ny))
                        country.append((nx, ny))
    return country

cnt = 0
while 1:
    flag = False
    visit = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if visit[x][y] == 0:
                visit[x][y] = 1
                temp = bfs(x, y)
                
                if len(temp) > 1:
                    flag = True
                    idx = len(temp)
                    tmp = 0
                    for i in range(idx):
                        tmp += graph[temp[i][0]][temp[i][1]]
                    for i in range(idx):
                        graph[temp[i][0]][temp[i][1]] = tmp // idx

    if not flag:
        break
    cnt += 1

print(cnt)