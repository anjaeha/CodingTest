# 모든 구름이 d방향으로 s칸 이동
# 비가 내려 칸 바구니에 물의 양 + 1
# 구름 사라짐
# 방금 증가한 칸에서 물복사 -> 이웃한 대각선 바구니에 물이 있는 수만큼 물의 양 증가 (범위 벗어나지 않음)
# 바구니의 물이 2이상이면 구름이 생기고, 물의 양 -2, 구름이 사라진곳에서는 생기지 않음

dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dir = [list(map(int, input().split())) for _ in range(m)] # 방향d, 거리s

cloud = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)] # 비바라기하면 (n, 1), (n, 2), (n - 1, 1), (n - 1, 2)에 비구름

def cloud_move(arr, d, s): # 구름, 방향, 거리
    new_cloud = []
    for x, y in arr:
        nx = (x + dx[d] * s) % n
        ny = (y + dy[d] * s) % n

        new_cloud.append((nx, ny))
    return new_cloud

def rain(arr):
    for x, y in arr:
        graph[x][y] += 1

def water_copy(arr):
    for x, y in arr:
        for d in range(2, 9, 2):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > 0:
                    graph[x][y] += 1

def make_cloud(arr):
    new_cloud = []
    for x in range(n):
        for y in range(n):
            if graph[x][y] >= 2:
                if (x, y) not in arr:
                    new_cloud.append((x, y))
                    graph[x][y] -= 2
    return new_cloud

for d, s in dir:
    cloud = cloud_move(cloud, d, s)
    rain(cloud)
    water_copy(cloud)
    cloud = make_cloud(cloud)

result = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] > 0:
            result += graph[i][j]

print(result)