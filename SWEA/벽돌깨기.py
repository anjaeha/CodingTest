# 구슬은 N번만 쏠 수 있으며 W * H의 벽이 주어짐
# 구슬은 좌 우로만 움직이며, 맨 위에 있는 벽돌만 깨트릴 수 있음.
# 벽돌은 1 ~ 9로 표현, 명중하면 상하좌우로 -1칸 만큼 같이 제거 (숫자 크기만큼)
from collections import deque
from copy import deepcopy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def make_candi(depth):
    global temp, candi
    if depth == k:
        candi.append(list(temp))
        return

    for i in range(m):
        temp.append(i)
        make_candi(depth + 1)
        temp.pop()

def crush(idx):
    visit = [[False] * m for _ in range(n)]
    q = deque()
    for i in range(n):
        if graph[i][idx] == 0:
            continue
        else:
            q.append((i, idx, graph[i][idx]))
            break

    while q:
        x, y, cnt = q.popleft()
        for i in range(cnt):
            for d in range(4):
                nx = x + (dx[d] * i)
                ny = y + (dy[d] * i)

                if 0 <= nx < n and 0 <= ny < m:
                    if not visit[nx][ny] and graph[nx][ny] != 0:
                        if graph[nx][ny] == 1:
                            graph[nx][ny] = 0
                            visit[nx][ny] = True
                        else:
                            size = graph[nx][ny]
                            graph[nx][ny] = 0
                            visit[nx][ny] = True
                            q.append((nx, ny, size))
    gravity()

def gravity():
    global graph
    s = [[0] * m for _ in range(n)]
    for i in range(m):
        q = deque()
        for j in range(n - 1, -1, -1):
            if graph[j][i] != 0:
                q.append(graph[j][i])

        for j in range(n - 1, -1, -1):
            if q:
                s[j][i] = q.popleft()
            else:
                break

    graph = s

def check():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                cnt += 1
    return cnt



T = int(input())

for tc in range(1, T + 1):
    k, m, n = map(int, input().split()) # m이 가로, n이 세로
    graph = [list(map(int, input().split())) for _ in range(n)]
    temp_graph = [item[:] for item in graph]
    # 떨어트릴수 있는 모든 경우의 수
    temp = []
    candi = []
    make_candi(0)
    result = 1000
    for case in range(len(candi)):
        graph = [item[:] for item in temp_graph]
        arr = candi[case]

        for i in range(k):
            crush(arr[i])

        temp = check()
        if result > temp:
            result = temp
        if result == 0:
            break



    print("#%d %d" %(tc, result))