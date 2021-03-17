from collections import deque
queue = deque()
n, m = map(int, input().split())


t = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    t.append(list(map(int, input())))


def bfs(x, y):    
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and t[nx][ny] == 1:
                t[nx][ny] = t[x][y] + 1
                queue.append((nx, ny))
    return t[n-1][m-1]

print(bfs(0,0))

