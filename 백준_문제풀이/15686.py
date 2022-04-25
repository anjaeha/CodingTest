n, m = map(int, input().split()) # N * N의 그래프 M개의 치킨집
graph = [list(map(int, input().split())) for _ in range(n)]

h_pos = [] # 집의 좌표
c_pos = [] # 치킨집 좌표
for x in range(n):
    for y in range(n):
        if graph[x][y] == 1:
            h_pos.append((x, y))
        elif graph[x][y] == 2:
            c_pos.append((x, y))

candi = []
temp = []
visit = [False] * len(c_pos)
def make_candi(depth):
    if depth == m:
        candi.append(list(temp))
        return

    for i in range(len(c_pos)):
        if visit[i]:
            continue
        visit[i] = True
        temp.append(c_pos[i])
        make_candi(depth + 1)
        temp.pop()
        for j in range(i + 1, len(c_pos)):
            visit[j] = False
make_candi(0)

result = 987654321
for idx in range(len(candi)):
    now = candi[idx]
    SUM = 0
    for x, y in h_pos: # 집의 위치
        temp = 987654321
        for r, c in now: # 남은 치킨집의 위치
           temp = min(temp, abs(x - r) + abs(y - c))
        SUM += temp
    result = min(result, SUM)
print(result)