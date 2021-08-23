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