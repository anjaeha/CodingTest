from collections import deque
queue = deque()

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())

t = []

for i in range(n):
    t.append(list(map(int, input())))


def bfs(x, y):
    queue.append((x, y))
    
    while queue:
        a, b = queue.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < n and 0 <= ny < m and t[nx][ny] == 1:
                t[nx][ny] = t[a][b] + 1
                queue.append((nx, ny))

    return t[n-1][m-1]

print(bfs(0,0))