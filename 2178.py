def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
            # 미로를 벗어나면 continue
                continue
            if arr[nx][ny] == 0:
            # 이동할 수 없는 칸인 0이어도 continue
                continue
            if arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] + 1
                queue.append((nx, ny))
    return arr[N - 1][M - 1]


from collections import deque

N, M = map(int, input().split())

arr = []
for i in range(N):
    arr.append(list(map(int, input())))
    # 공백없이 0 또는 1로 값을 받을거라 append로 값을 받음

dx = [-1, 1, 0, 0]
# 상 하 좌 우
# X값이 바뀌면 y측으로 이동함
dy = [0, 0, -1, 1]
# y 값이 바뀌면 x축으로 이동함

print((bfs(0,0)))