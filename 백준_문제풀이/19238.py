# N * N 크기의 지도
# M명의 승객을 태우는 것이 목표
# 현재 위치에서 가장 짧은 승객을 고름, x값이 작고, y값이 작은 순서로 승객 선택
# 연료는 한칸 이동할때마다 1소모
# 승객을 목적지로 이동 시키면, 이동하면서 소모한 연료 양의 두 배가 충전됨
# 이동 도중 바닥나면 이동 실패, 업무 종료
# 목적지까지 데려다 줄 수 있는지 확인하여 남은 연료의 양 출력
from collections import deque
def dist(x, y):
    # 현재 위치에서 모든 지점까지의 거리 구하기
    visit = [[-1] * n for _ in range(n)]
    q = deque()
    q.append((x, y))
    visit[x][y] = 0
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 0 and visit[nx][ny] == -1:
                    visit[nx][ny] = visit[x][y] + 1
                    q.append((nx, ny))
    # 어떤 승객을 태우러 갈지 결정
    MIN = int(1e9)
    idx = -1
    for i in range(len(passenger)):
        temp = passenger[i]
        sx, sy = temp[0], temp[1]
        if visit[sx][sy] < MIN:
            MIN = visit[sx][sy]
            idx = i

    return idx, MIN

# 필요한 연료 구하기
def fuel(sx, sy, ex, ey):
    visit = [[-1] * n for _ in range(n)]
    visit[sx][sy] = 0
    q = deque()
    q.append((sx, sy))

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 0 and visit[nx][ny] == -1:
                    visit[nx][ny] = visit[x][y] + 1
                    q.append((nx, ny))
    return visit[ex][ey]

n, m, k = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = [list(map(int, input().split())) for _ in range(n)] # 0 - 빈칸, 1 - 벽
tx, ty = map(int, input().split())
tx, ty = tx - 1, ty - 1

passenger = []
for _ in range(m):
    sx, sy, ex, ey = map(int, input().split())
    passenger.append((sx - 1, sy - 1, ex - 1, ey - 1))

passenger.sort(key = lambda x : (x[0], x[1]))

for i in range(m):
    idx, idx_cost = dist(tx, ty)
    # 갈수 없는 곳이라면 종료
    if idx_cost == -1:
        k = -1
        break
    k -= idx_cost # 찾아가는데 연료 사용

    need_fuel = fuel(passenger[idx][0], passenger[idx][1], passenger[idx][2], passenger[idx][3]) # 손님을 태우고 이동하는데 필요한 연료
    if k < need_fuel:
        k = -1
        break
    k += need_fuel
    tx, ty = passenger[idx][2], passenger[idx][3]
    passenger.pop(idx)

print(k)