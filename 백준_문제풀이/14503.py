n, m = map(int, input().split())
r, c, dir = map(int, input().split()) # 청소기 좌표(r, c), 방향 dir
graph = [list(map(int, input().split())) for _ in range(n)] # 0 - 빈칸, 1 - 벽

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def clean(x, y, dir):
    graph[x][y] = 2 # 청소한 위치 표시

    for d in range(4):
        dir = (dir - 1) % 4 # 현재 방향기준 왼쪽부터 탐색 (2 조건)
        nx = x + dx[dir]
        ny = y + dy[dir]

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0: # 청소하지 않은 공간이 있다면 청소 (2 - a 조건)
                clean(nx, ny, dir)
                return

    nx = x - dx[dir] # 뒤로 이동
    ny = y - dy[dir]

    if graph[nx][ny] == 1: # 뒤쪽 방향이 벽이면 작동 종료 (이미 네 방향 모두 청소가 되어있는 상태로 2 - d 조건)
        return

    clean(nx, ny, dir) # 뒤로 이동해서 청소 시작 (2 - c 조건)

clean(r, c, dir) # 청소기 실행
result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            result += 1
print(result)