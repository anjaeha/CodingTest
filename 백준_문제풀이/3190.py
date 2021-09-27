
from collections import deque
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# 동, 남, 서, 북

n = int(input()) # 보드의 크기
graph = [[0] * n for _ in range(n)]
k = int(input()) # 사과의 개수
for _ in range(k):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 2 # 사과는 2

move_dir = []
m = int(input()) # 방향 전환 횟수
for _ in range(m):
    x, y = input().split()
    move_dir.append((int(x), y))

cnt = 0
d = 0

q = deque()
q.append((0, 0))
idx = 0
while 1:
    cnt += 1
    x, y = q[-1][0], q[-1][1]
    
    nx = x + dx[d]
    ny = y + dy[d]

    if 0 <= nx < n and 0 <= ny < n:
        if (nx, ny) in q:
            break
        if graph[nx][ny] == 2:
            q.append((nx, ny))
            graph[nx][ny] = 0
        else:
            q.popleft()
            q.append((nx, ny))
    else:
        break
    
    if cnt <= move_dir[-1][0]:
        if cnt == move_dir[idx][0]:
            if move_dir[idx][1] == 'L':
                d = (d - 1) % 4
            else:
                d = (d + 1) % 4
            idx += 1

print(cnt)