import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

copydx = [-1, -1, 1, 1]
copydy = [-1, 1, -1, 1]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
move = [list(map(int, input().split())) for _ in range(m)]

cloud = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]]

def makeCloud(graph):
    cloud = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= 2 and visit[i][j] == False:
                graph[i][j] -= 2
                cloud.append((i, j))

    return cloud

for case in range(m):
    visit = [[False] * n for _ in range(n)]
    dir, dis = move[case]
    nx = dx[dir]
    ny = dy[dir]

    newCloud = []
    for cloud_x, cloud_y in cloud:
        cloud_x = (cloud_x + nx * dis) % n
        cloud_y = (cloud_y + ny * dis) % n
        
        graph[cloud_x][cloud_y] += 1
        visit[cloud_x][cloud_y] = True
        newCloud.append((cloud_x, cloud_y))


    for x, y in newCloud:
        cnt = 0
        for i in range(4):
            searchx = x + copydx[i]
            searchy = y + copydy[i]

            if 0 <= searchx < n and 0 <= searchy < n:
                if graph[searchx][searchy] > 0:
                    cnt += 1

        graph[x][y] += cnt

    cloud = makeCloud(graph)
    

result = 0
for i in range(n):
    for j in range(n):
        result += graph[i][j]

print(result)


"""
# 모든 구름이 d방향으로 s칸 이동
# 구름에서 비가 내려서 물의 양이 1 증가
# 구름이 사라짐
# 물복사버그 마법 -> 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 물 증가
# 바구니에 저장된 물의 양이 2이상인 모든 칸에 구름이 생김, 물의 양 2감소, 구름이 사라진 칸에서는 불가

dx8 = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy8 = [0, -1, -1, 0, 1, 1, 1, 0, -1]

dx4 = [-1, -1, 1, 1]
dy4 = [-1, 1, -1, 1]

def move(arr, d, s):
    com = []
    for x, y in arr:
        nx = x + (dx8[d] * s)
        ny = y + (dy8[d] * s)

        com.append((nx % n, ny % n))
    return com


def rain(arr):
    for x, y in arr:
        graph[x][y] += 1
    return


def copy_water(arr):
    global graph
    s = [item[:] for item in graph]
    for x, y in arr:
        cnt = 0
        for d in range(4):
            nx = x + dx4[d]
            ny = y + dy4[d]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > 0:
                    cnt += 1
        s[x][y] += cnt
    graph = s


def make_cloud(arr):
    temp = []
    for i in range(n):
        for j in range(n):
            if (i, j) not in arr:
                if graph[i][j] >= 2:
                    graph[i][j] -= 2
                    temp.append((i, j))
    return temp


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cloud_move = [list(map(int, input().split())) for _ in range(m)]

cloud = [(n - 1, 0), (n - 2, 0), (n - 1, 1), (n - 2, 1)]


for case in range(m):
    cur = cloud_move[case]
    cloud = move(cloud, cur[0], cur[1])
    rain(cloud)
    copy_water(cloud)
    cloud = make_cloud(cloud)


result = 0
for i in range(n):
    for j in range(n):
        if graph[i][j]:
            result += graph[i][j]


print(result)
"""