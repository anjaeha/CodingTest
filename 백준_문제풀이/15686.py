n, m = map(int, input().split()) # 치킨집의 최대 개수 M
graph = [list(map(int, input().split())) for _ in range(n)] # 0 - 빈칸, 1 - 집, 2 - 치킨집
# 집과 가장 가까운 치킨집 사이의 거리의 합 => 최소 구하기

chicken = []
house = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chicken.append((i, j))
        elif graph[i][j] == 1:
            house.append((i, j))

candi = []
temp = []
visit = [False] * len(chicken)
def make_candi(cnt):
    if cnt == m:
        candi.append(list(temp))
        return

    for i in range(len(chicken)):
        if visit[i]:
            continue
        visit[i] = True
        temp.append(chicken[i])
        make_candi(cnt + 1)
        temp.pop()
        for j in range(i + 1, len(chicken)):
            visit[j] = False
make_candi(0)

MIN = int(1e9)
for i in range(len(candi)):
    temp = candi[i]
    SUM = 0
    for x in range(len(house)):
        cnt = int(1e9)
        for y in range(m):
            cnt = min((abs(house[x][0] - candi[i][y][0]) + abs(house[x][1] - candi[i][y][1])), cnt)
        SUM += cnt
    MIN = min(MIN, SUM)

print(MIN)