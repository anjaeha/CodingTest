# N * N 크기의 지도
# M명의 승객을 태우는 것이 목표
# 현재 위치에서 가장 짧은 승객을 고름, x값이 작고, y값이 작은 순서로 승객 선택
# 연료는 한칸 이동할때마다 1소모
# 승객을 목적지로 이동 시키면, 이동하면서 소모한 연료 양의 두 배가 충전됨
# 이동 도중 바닥나면 이동 실패, 업무 종료
# 목적지까지 데려다 줄 수 있는지 확인하여 남은 연료의 양 출력
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m, k = map(int, input().split()) # 지도의 크기, 승객의 수, 최초 연료
graph = [list(map(int, input().split())) for _ in range(n)]
start_x, start_y = map(int, input().split()) # 택시의 시작 위치
start_x, start_y = start_x - 1, start_y - 1
p = deque()
for i in range(m):
    sx, sy, ex, ey = map(int, input().split())
    p.append((sx - 1, sy - 1, ex - 1, ey - 1))

def find_p(x, y): # 현재 위치에서 승객까지의 이동거리 찾기 (승객 선택하는 함수)
    q = deque()
    q.append((x, y))
    s = [[-1] * n for _ in range(n)]
    visit = [[False] * n for _ in range(n)]
    s[x][y] = 0
    visit[x][y] = True
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 0 and not visit[nx][ny]:
                    s[nx][ny] = s[x][y] + 1
                    visit[nx][ny] = True
                    q.append((nx, ny))
    dist = []
    for i in range(len(p)):
        cur = p[i]
        if s[cur[0]][cur[1]] == -1:
            continue
        dist.append((s[cur[0]][cur[1]], cur[0], cur[1], cur[2], cur[3]))

    dist.sort(key = lambda x : (x[0], x[1], x[2]))
    if not dist: # 현재 위치에서 이동시킬 고객이 없으면 False값 리턴해줌.
        return False
    return dist[0]

def calc_food(sx, sy, ex, ey): # 시작위치에서 도착위치까지의 거리 계산
    q = deque()
    q.append((sx, sy))
    s = [[-1] * n for _ in range(n)]
    visit = [[False] * n for _ in range(n)]
    visit[sx][sy] = True
    s[sx][sy] = 0
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 0 and not visit[nx][ny]:
                    visit[nx][ny] = True
                    s[nx][ny] = s[x][y] + 1
                    q.append((nx, ny))
    return s[ex][ey]

flag = True
for case in range(m):
    cur = find_p(start_x, start_y) # 현재 위치에서 최단 경로에 있는 승객 구함
    if not cur: # 현재 위치에서 이동할 수 있는 승객이 없으면 종료
        flag = False
        break
    food = calc_food(cur[1], cur[2], cur[3], cur[4])
    if food == -1: # 이동할 수 없는 곳에 있으면 종료
        flag = False
        break

    k -= cur[0]
    if k < food: # 현재 가지고 있는 연료보다 필요한 연료가 더 크면 운행 종료
        flag = False
        break
    else:
        k += food
        start_x, start_y = cur[3], cur[4]
        cc = p.index((cur[1], cur[2], cur[3], cur[4]))
        del p[cc]



if flag:
    print(k)
else:
    print(-1)