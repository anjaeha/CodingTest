# 가장 높은 봉우리에서 시작
# 가로 또는 세로 방향으로 연결, 반드시 낮은 지형으로 이동해야함.
# 한 곳을 정해서 K만큼 깎는 공사 가능
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def search(x, y, graph):
    q = deque()
    q.append((x, y, 1))
    length = -1
    while q:
        x, y, cnt = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] < graph[x][y]:
                    q.append((nx, ny, cnt + 1))
    length = max(length, cnt)
    return length

T = int(input())

for tc in range(1, T + 1):
    result = -1
    n, k = map(int, input().split()) # N * N 그래프에서 최대 K만큼 깎을 수 있다.
    graph = [list(map(int, input().split())) for _ in range(n)]
    MAX = -1
    for i in range(n):
        for j in range(n):
            MAX = max(MAX, graph[i][j])
    temp_graph = [item[:] for item in graph]

    for i in range(n):
        for j in range(n):
            if graph[i][j] != MAX: # 시작 위치 (정상에서만 시작 가능)
                continue
            for x in range(n):
                for y in range(n): # 깎는 위치
                    for depth in range(k + 1):
                        temp_graph[x][y] -= depth
                        temp = search(i, j, temp_graph)
                        temp_graph[x][y] += depth
                        result = max(result, temp)

    print("#%d %d" %(tc, result))