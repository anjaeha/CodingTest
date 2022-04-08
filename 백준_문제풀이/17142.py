from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

vir_pos = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            vir_pos.append((i, j))

candi = []
temp = []
visit = [False] * len(vir_pos)
def make_candi(depth):
    if depth == m:
        candi.append(list(temp))
        return

    for i in range(len(vir_pos)):
        if visit[i]:
            continue
        visit[i] = True
        temp.append(vir_pos[i])
        make_candi(depth + 1)
        temp.pop()
        for j in range(i + 1, len(vir_pos)):
            visit[j] = False
make_candi(0)

def check():
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0 and count[i][j] == -1:
                return False
    return True

result = int(1e9)
for idx in range(len(candi)):
    now = candi[idx]
    q = deque()
    visit = [[False] * n for _ in range(n)]
    count = [[-1] * n for _ in range(n)]
    for x, y in now:
        count[x][y] = 0
        q.append((x, y))
        visit[x][y] = True
    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if not visit[nx][ny] and graph[nx][ny] != 1:
                    count[nx][ny] = count[x][y] + 1
                    visit[nx][ny] = True
                    q.append((nx, ny))
    if not check():
        continue
    MAX = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                MAX = max(MAX, count[i][j])
    result = min(result, MAX)

print(result if result != int(1e9) else -1)