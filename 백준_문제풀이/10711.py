
from collections import deque

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

result = 0
q = deque()

cnt = 0
s = [[0] * m for _ in range(n)]
for x in range(n):
    for y in range(m):
        if graph[x][y] == '.':
            q.append((x, y))
            graph[x][y] = 0
        else:
            graph[x][y] = int(graph[x][y])
# 모래성의 빈칸을 0으로 설정해준다.


# 무너진 모래성의 좌표를 기준으로 8방향을 탐색한다.
while len(q):
    x, y = q.popleft()
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m: # 좌표안에 0이 아닌 것이 있다면 1을 빼준다.
            if graph[nx][ny] != 0:
                graph[nx][ny] -= 1
                if graph[nx][ny] == 0: # 그리고 만약 0이면 (무너졌다면) 전 좌표에서 1을 더한값을 저장해준뒤
                    s[nx][ny] = s[x][y] + 1
                    q.append((nx, ny)) # q에 추가를 해준다. 새로 무너진 것이므로 다시 계산해주기 위함.

# 무너진 순서인 s를 돌며 최대값을 구해준다.
for i in range(n):
    for j in range(m):
        if result < s[i][j]:
            result = s[i][j]
print(result)