from collections import deque

n = int(input())
graph = [[0] * 101 for _ in range(101)]
dx = [0, -1, 0, 1] # 우, 상, 좌, 하
dy = [1, 0, -1, 0]

def curve(x, y, d, g):
    arr = [] # 역대 방향 저장하기
    graph[x][y] = 1
    q = deque()
    q.append(d)
    for idx in range(g + 1):
        q.extend(arr[::-1])
        while q:
            d = q.popleft()
            x = x + dx[d]
            y = y + dy[d]
            if 0 <= x <= 100 and 0 <= y <= 100:
                arr.append((d + 1) % 4)
                graph[x][y] = 1

for _ in range(n):
    y, x, d, g = map(int, input().split()) # 좌표(x, y) 시작방향, 세대
    curve(x, y, d, g)

result = 0
for x in range(100):
    for y in range(100):
        if graph[x][y]:
            if graph[x + 1][y] and graph[x][y + 1] and graph[x + 1][y + 1]:
                result += 1

print(result)