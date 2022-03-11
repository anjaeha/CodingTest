n, m = map(int, input().split()) # 치킨집의 최대 개수 M
graph = [list(map(int, input().split())) for _ in range(n)] # 빈 칸 - 0, 집 - 1, 치킨집 - 2

house_pos = []
chicken_pos = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house_pos.append((i, j))
        elif graph[i][j] == 2:
            chicken_pos.append((i, j))

candi = []
temp = []
visit = [False] * len(chicken_pos)

def dfs(depth):
    if depth == m:
        candi.append(list(temp))
        return
    for i in range(len(chicken_pos)):
        if visit[i]:
            continue
        visit[i] = True
        temp.append(chicken_pos[i])
        dfs(depth + 1)
        temp.pop()
        for j in range(i + 1, len(chicken_pos)):
            visit[j] = False

dfs(0)

MIN = int(1e9)
for case in range(len(candi)):
    dist = 0
    for i in range(len(house_pos)):
        hx, hy = house_pos[i]
        temp = int(1e9)
        for j in range(m):
            cx, cy = candi[case][j]
            temp = min(abs(hx - cx) + abs(hy - cy), temp)
        dist += temp

    MIN = min(MIN, dist)
print(MIN)