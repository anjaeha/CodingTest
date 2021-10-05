dx = [-1, 1, 1, -1]
dy = [1, 1, -1, -1]
# 우상, 우하, 좌하, 좌상

def move(x, y):
    global result
    ex, ey = x, y
    visit = [graph[x][y]]
    d = 0
    q = [(x, y, d, visit)]

    while q:
        cur = q.pop()
        x, y, d, visit = q.pop()
        
        if d > 3:
            continue

        nx = x + dx[d]
        ny = y + dy[d]

        if nx == ex and ny == ey and d == 3:
            result = max(result, len(visit))
            continue
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] not in visit:
            visit.append(graph[nx][ny])
            q.append((nx, ny, d, visit[:]))
            q.append((nx, ny, d + 1, visit[:]))


T = int(input())

for case in range(1, T + 1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]

    result = -1
    for i in range(n):
        for j in range(n):
            move(i, j)

    print("#%d %d" %(case, result))