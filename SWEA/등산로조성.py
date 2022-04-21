from collections import deque

def find(x, y):
    global result

    q = deque()
    q.append((x, y, 1))

    while q:
        x, y, cnt = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[x][y] > graph[nx][ny]:
                    q.append((nx, ny, cnt + 1))

    result = max(result, cnt)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for tc in range(T):
    n, k = map(int, input().split()) # K 깊이만큼 공사가능
    graph = [list(map(int, input().split())) for _ in range(n)]

    MAX = -1
    for x in range(n):
        for y in range(n):
            if graph[x][y] > MAX:
                MAX = graph[x][y]

    start = []
    for x in range(n):
        for y in range(n):
            if graph[x][y] == MAX:
                start.append((x, y))

    result = 0
    for r in range(n):
        for c in range(n):
            for idx in range(k + 1):
                graph[r][c] -= idx
                for x, y in start:
                    find(x, y)
                graph[r][c] += idx

    print("#%d %d" %(tc + 1, result))