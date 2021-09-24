n, east, west, south, north = map(int, input().split())
p = [east / 100, west / 100, south / 100, north / 100]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visit = [[0] * (2 * n + 1) for _ in range(2 * n + 1)] # 방문 여부를 파악하기 위함
visit[n][n] = 1 # (0, 0)에서 -로 가지 못하기에 (n, n)에서 시작하는 것으로 생각함.

result = 0
def dfs(x, y, percent, depth):
    global result
    if depth == n: # n번 움직이면 확률을 구해줌.
        result += percent
        return
    
    # 동서남북으로 움직이며 방문하지 않았을 경우에만 dfs함수 반복
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 2 * n + 1 and 0 <= ny < 2 * n + 1:
            if visit[nx][ny] == 0:
                visit[nx][ny] = 1
                dfs(nx, ny, percent * p[i], depth + 1)
                visit[nx][ny] = 0
            else:
                continue
dfs(n, n, 1, 0)
print(result)