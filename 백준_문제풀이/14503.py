n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 북, 동, 남, 서

def robot_move(x, y, dir):
    if graph[x][y] == 0: # 0이면 청소
        graph[x][y] = 2

    for i in range(4): # 4방향을 돌며 (왼쪽 방향)
        dir = (dir - 1) % 4
        nx = x + dx[dir]
        ny = y + dy[dir]

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0: # 0이면 다시 청소 시작
                robot_move(nx, ny, dir)
                return

	# 4방향 모두 청소하지 못했으면 한칸 뒤로 물러남.
    nx = x - dx[dir]
    ny = y - dy[dir]
    
	# 물러났는데 벽이면 종료
    if graph[nx][ny] == 1:
        return
        
    robot_move(nx, ny, dir)

robot_move(r, c, d)
# 청소한 칸의 개수 구하기
result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            result += 1

print(result)