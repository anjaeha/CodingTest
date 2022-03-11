n = int(input()) # 드래곤 커브의 개수

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
# 우, 상, 좌, 하

graph = [[False] * 101 for _ in range(101)]

# 드래곤 커브
for tc in range(n):
    y, x, d, g = map(int, input().split()) # 시작좌표 (y, x), 시작방향 d, 세대 g
    q = []
    q.append(d)
    graph[x][y] = True
    x, y = x + dx[d], y + dy[d]
    graph[x][y] = True # 0세대
    temp = [d]

    for i in range(g):
        while q:
            dir = q.pop()
            x = x + dx[(dir + 1) % 4]
            y = y + dy[(dir + 1) % 4]
            graph[x][y] = True
            temp.append((dir + 1) % 4)
        q = temp[:]


result = 0
for i in range(100):
    for j in range(100):
        if graph[i][j]:
            if graph[i + 1][j] and graph[i][j + 1] and graph[i + 1][j + 1]:
                result += 1
print(result)