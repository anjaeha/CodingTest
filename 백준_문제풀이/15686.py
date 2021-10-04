n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

house = {}
chicken = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house[i, j] = 1
        elif graph[i][j] == 2:
            chicken.append((i, j))

def make_candi(depth): # 살려둘 치킨집 경우의 수 구하기
    global temp
    if depth == m:
        candi.append(list(temp))
        return
    
    for i in range(len(chicken)):
        if visit[i]:
            continue

        visit[i] = True
        temp.append(i)
        make_candi(depth + 1)
        temp.pop()
        for j in range(i + 1, len(chicken)):
            visit[j] = False
visit = [False] * len(chicken)
candi = []
temp = []
make_candi(0)



MIN = 10000000 # 치킨거리 최소값 구하기
for idx in range(len(candi)): # 경우의 수를 하나씩 해보며
    chicken_house = candi[idx]
    cnt = 0
    for xy, val in house.items(): # (집 위치에서 남아있는 치킨집 사이의 최소값)
        house_x, house_y = xy[0], xy[1]
        house_dist = 100
        for i in range(m):
            r, c = chicken[chicken_house[i]][0], chicken[chicken_house[i]][1]
            temp = abs(house_x - r) + abs(house_y - c)
            house_dist = min(temp, house_dist)
        cnt += house_dist
    MIN = min(MIN, cnt) # 치킨 거리 중 최소값 구하기

print(MIN)