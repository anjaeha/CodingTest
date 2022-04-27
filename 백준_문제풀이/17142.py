from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
# 0 - 빈칸, 1 - 벽, 2 - 바이러스

virus_pos = []
for x in range(n):
    for y in range(n):
        if graph[x][y] == 2:
            virus_pos.append((x, y))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

candi = []
temp = []
visit = [False] * len(virus_pos)
def make_candi(depth):
    if depth == m:
        candi.append(list(temp))
        return

    for i in range(len(virus_pos)):
        if visit[i]:
            continue

        visit[i] = True
        temp.append(virus_pos[i])
        make_candi(depth + 1)
        temp.pop()
        for j in range(i + 1, len(virus_pos)):
            visit[j] = False

make_candi(0)
copy_graph = [i[:] for i in graph]
result = 987654321
for idx in range(len(candi)):
    cost = [[-1] * n for _ in range(n)]
    now = candi[idx]
    q = deque(now)
    for r, c in now:
        cost[r][c] = 0
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] != 1 and cost[nx][ny] == -1:
                    cost[nx][ny] = cost[x][y] + 1
                    q.append((nx, ny))

    time = 0
    flag = False
    for x in range(n):
        for y in range(n):
            if graph[x][y] == 0:
                if cost[x][y] == -1:
                    flag = True
                time = max(time, cost[x][y])
    if not flag:
        result = min(result, time)

print(result if result != 987654321 else -1)