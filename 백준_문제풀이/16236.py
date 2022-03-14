from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            graph[i][j] = 0
            sx, sy = i, j
size = 2

result = 0
def search():
    global result
    q = deque()
    q.append((sx, sy))
    visit = [[-1] * n for _ in range(n)] # 현재 위치에서 거리 구하기
    can_eat = [[False] * n for _ in range(n)] # 먹을 수 있는지 확인
    visit[sx][sy] = 0
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] <= size and visit[nx][ny] == -1:
                    visit[nx][ny] = visit[x][y] + 1
                    q.append((nx, ny))
                    if 0 < graph[nx][ny] < size:
                        can_eat[nx][ny] = True

    MIN = int(1e9)
    mx, my = -1, -1
    for i in range(n):
        for j in range(n):
            if can_eat[i][j]: # 먹을 수 있는 곳이면
                if visit[i][j] < MIN: # 최소거리이면서 가장 왼쪽, 가장 위에 있는 곳을 구해야함
                    MIN = visit[i][j]
                    mx, my = i, j

    if (mx, my) == (-1, -1): # 만약, 최소거리가 없으면 종료
        return False

    return (visit[mx][my], mx, my)


size_cnt = 0
while 1:
    res = search()
    if res == False:
        break

    count, mx, my = res

    result += count
    sx, sy = mx, my # 상어의 위치를 변경해주고
    graph[sx][sy] = 0 # 먹었으니 0으로 변경
    size_cnt += 1 # 몇개 먹었는지 확인
    if size_cnt == size: # 먹은 개수가 몸의 크기와 같으면
        size += 1 # 사이즈 키워주고 0으로 초기화
        size_cnt = 0

print(result)