from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())

s = [list(map(int, input().strip())) for _ in range(n)]

count = []

def bfs(a, b):
    cnt = 1
    q = deque()
    q.append((a, b))
    s[a][b] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if s[nx][ny] == 1:
                q.append((nx, ny))
                s[nx][ny] = 0
                cnt += 1
    
    count.append(cnt)



for i in range(n):
    for j in range(n):
        if s[i][j] == 1:
            bfs(i, j)


count.sort()
print(len(count))
for i in count:
    print(i)

"""
def dfs(x, y):
    global cnt
    graph[x][y] = 0
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 1:
                dfs(nx, ny)
                cnt += 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

answer = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt = 1
            dfs(i, j)
            answer.append(cnt)

print(len(answer))
answer.sort()
for i in answer:
    print(i)
"""