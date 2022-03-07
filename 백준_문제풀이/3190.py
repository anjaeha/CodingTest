from collections import deque

# 벽 또는 몸과 부딪히면 게임 종료

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
# 우, 상, 좌, 하

d = 0 # 기본 방향 오른쪽

n = int(input())
k = int(input())
graph = [[0] * n for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = 1 # 사과

l = int(input())
dir = [list(input().split()) for _ in range(l)]

q = deque()
q.append((0, 0))
x, y = 0, 0
def move():
    global x, y
    x, y = x + dx[d], y + dy[d]

    if 0 <= x < n and 0 <= y < n:
        if (x, y) not in q:
            if graph[x][y] == 1:
                q.append((x, y))
                graph[x][y] = 0
            else:
                q.append((x, y))
                q.popleft()
            return True
        else:
            return False
    else:
        return False

change = 0
def change_dir():
    global d, change
    if change >= l:
        return
    if answer == int(dir[change][0]):
        if dir[change][1] == 'D':
            d = (d - 1) % 4
        else:
            d = (d + 1) % 4
        change += 1

answer = 0
while 1:
    answer += 1
    if not move():
        break
    change_dir()

print(answer)