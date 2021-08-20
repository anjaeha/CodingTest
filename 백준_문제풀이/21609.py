#적어도 하나의 일반 블록, (같은 색이어야함.)
# 검은색 블록X 무지개블록은 숫자 상관 X
# 블록의 개수는 2이상, 상하좌우로 이어져야함.
# 기준 블록은 무지개블록이 아닌 블록 중 X, Y 값이 작은거로
# 1. 가장 큰 블록그룹 찾고 > 무지개 블록 수가 많은 그룹 > X큰 > Y큰
# 2. 1의 블록 제거, 제거한 블록의 수 ** 2 점수 획득
# 3. 중력 작용,
# 4. 90% 반시계로 회전
# 5. 중력 작용,
# 중력이 작용하면, 검은색 블록 제외하고 밑으로 이동,

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

def bfs(x, y, color):
    q = deque()
    q.append((x, y))
    
    block_cnt, rainbow_cnt = 1, 0
    blocks, rainbows = [[x, y]], []

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if visit[nx][ny] == False:
                    if graph[nx][ny] == color or graph[nx][ny] == 0:
                        if graph[nx][ny] == 0:
                            rainbow_cnt += 1
                            rainbows.append((nx, ny))
                        else:
                            blocks.append((nx, ny))
                        q.append((nx ,ny))
                        block_cnt += 1
                        visit[nx][ny] = True

    for x, y in rainbows:
        visit[x][y] = False

    return [block_cnt, rainbow_cnt, blocks + rainbows]

    

def gravity(arr):
    for i in range(n -2, -1, -1):
        for j in range(n):
            if arr[i][j] > -1:
                r = i
                while 1:
                    if 0 <= r + 1 < n and arr[r+1][j] == -2:
                        arr[r+1][j] = arr[r][j]
                        arr[r][j] = -2
                        r += 1
                    else:
                        break


def rotate(arr):
    roate_graph = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            roate_graph[i][j] = graph[j][n - i - 1]

    return roate_graph


while 1:
    visit = [[False] * n for _ in range(n)]
    block = []
    for i in range(n):
        for j in range(n):
            if 0 < graph[i][j] <= m and not visit[i][j]:
                visit[i][j] = 1
                block_info = bfs(i, j, graph[i][j])
                if block_info[0] >= 2:
                    block.append(block_info)

    

    if not block:
        break
    block.sort(reverse=True)

    break_block = block[0][2]
    result += len(break_block) ** 2
    for x, y in break_block:
        graph[x][y] = -2


    gravity(graph)
    graph = rotate(graph)
    gravity(graph)

print(result)