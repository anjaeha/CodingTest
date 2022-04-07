n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


chicken_pos = []
house_pos = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house_pos.append((i, j))
        elif graph[i][j] == 2:
            chicken_pos.append((i, j))

visit = [False] * len(chicken_pos)
temp = []
candi = []
def make_candi(depth):
    if depth == m:
        candi.append(list(temp))
        return

    for i in range(len(chicken_pos)):
        if visit[i]:
            continue
        visit[i] = True
        temp.append(chicken_pos[i])
        make_candi(depth + 1)
        temp.pop()

        for j in range(i + 1, len(chicken_pos)):
            visit[j] = False
make_candi(0)

result = int(1e9)
for idx in range(len(candi)):
    now = candi[idx]
    SUM = 0
    for hx, hy in house_pos:
        MIN = int(1e9)
        for cx, cy in now:
           temp = abs(hx - cx) + abs(hy - cy)
           MIN = min(MIN, temp)
        SUM += MIN
    result = min(result, SUM)

print(result)