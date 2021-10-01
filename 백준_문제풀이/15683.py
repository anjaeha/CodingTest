from copy import deepcopy
n, m = map(int, input().split()) # 사무실의 크기
graph = [list(map(int, input().split())) for _ in range(n)] # 0은 빈칸, 6은 벽, 1~ 5는 CCTV

MIN = 100 # 사각지대의 개수
def check():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                cnt += 1
    return cnt

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

direct = [[], [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[0, 3], [0, 2], [1, 3], [1, 2]], [[0, 2, 3], [1, 2, 3], [0, 1, 3], [0, 1, 2]], [[0, 1, 2, 3]]]
# 1번은 상 / 하 / 좌 / 우
# 2번은 상, 하 / 좌, 우
# 3번은 상, 우 / 상, 좌 / 하, 우 / 하, 좌
# 4번은 상, 좌, 우 / 하, 좌, 우 / 상 하, 우 / 상, 하, 좌
# 5번은 상 하 좌 우 

camera = []
for i in range(n):
    for j in range(m):
        if 0 < graph[i][j] < 6:
            camera.append((i, j, graph[i][j]))


def fill(x, y, d):
    for i in d:
        nx, ny = x, y
        while 1:
            nx += dx[i]
            ny += dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != 6:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = '#'
                else:
                    break
            else:
                break

def dfs(depth):
    global MIN, graph
    if depth == len(camera):
        temp = check()
        MIN = min(MIN, temp)
        return

    temp_graph = deepcopy(graph)           
    x, y, dir = camera[depth]
    for i in direct[dir]:
        fill(x, y, i)
        dfs(depth + 1)
        graph = deepcopy(temp_graph)

dfs(0)
print(MIN)