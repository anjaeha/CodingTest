import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
temp = [[0] * m for _ in range(n)]
result = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)


def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1

    return score

def dfs(count):
    global result

    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = arr[i][j]

        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)

        result = max(result, get_score())
        return


    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                count += 1
                dfs(count)
                count -= 1
                arr[i][j] = 0

dfs(0)
print(result)


"""
from collections import deque
from copy import deepcopy

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

virus_pos = []

can_wall = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            can_wall.append((i, j))
        elif graph[i][j] == 2:
            virus_pos.append((i, j))


wall_pos = []
temp = []

visit = [False] * len(can_wall)
def make_candi(depth):
    global temp, wall_pos, visit
    if depth == 3:
        wall_pos.append(list(temp))
        return
    
    for i in range(len(can_wall)):
        if visit[i]:
            continue

        visit[i] = True
        temp.append(can_wall[i])
        make_candi(depth + 1)
        temp.pop()
        for j in range(i + 1, len(can_wall)):
            visit[j] = False
make_candi(0)


def virus_move():
    virus_visit = [[False] * m for _ in range(n)]
    q = deque()
    for i in range(len(virus_pos)):
        q.append(virus_pos[i])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and virus_visit[nx][ny] == False:
                    graph[nx][ny] = 2
                    virus_visit[nx][ny] = True
                    q.append((nx, ny))

    result = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                result += 1
    return result

MAX = -1
temp_graph = deepcopy(graph)
for case in range(len(wall_pos)):
    graph = deepcopy(temp_graph)
    idx = wall_pos[case]
    for x, y in idx:
        graph[x][y] = 1
    temp = virus_move()
    if MAX < temp:
        MAX = temp

print(MAX)
"""