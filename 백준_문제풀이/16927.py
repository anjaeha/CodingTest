from collections import deque

n, m, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def rotate(x, y, r):
    q = deque()
    q.append((graph[x][y]))
    s_x, s_y = x, y

    for nx in range(x + 1, n - x):
        q.append(graph[nx][s_y])
        s_x = nx
    for ny in range(y + 1, m - y):
        q.append(graph[s_x][ny])
        s_y = ny
    for nx in range(n - x - 2, x - 1, -1):
        q.append(graph[nx][s_y])
        s_x = nx
    for ny in range(m - y - 2, y, -1):
        q.append(graph[s_x][ny])
        s_y = ny
    
    for _ in range(r % len(q)):
        q.appendleft(q.pop())
    
    s_x, s_y = x, y
    graph[s_x][s_y] = q.popleft()
    for nx in range(x + 1, n - x):
        graph[nx][s_y] = q.popleft()
        s_x = nx
    for ny in range(y + 1, m - y):
        graph[s_x][ny] = q.popleft()
        s_y = ny
    for nx in range(n - x - 2, x - 1, -1):
        graph[nx][s_y] = q.popleft()
        s_x = nx
    for ny in range(m - y - 2, y, -1):
        graph[s_x][ny] = q.popleft()
        s_y = ny

for case in range(min(n, m) // 2):
    x, y = case, case
    rotate(x, y, r)

for i in graph:
    print(*i)