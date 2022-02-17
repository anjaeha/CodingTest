from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = []
def bfs(x, y):
    q = deque()
    q.append((x, y))
    count = 1
    graph[x][y] = 0

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    count += 1
                    graph[nx][ny] = 0
                    q.append((nx, ny))

    answer.append(count)
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            bfs(i, j)

if answer:
    print(len(answer))
    print(max(answer))
else:
    print(0)
    print(0)