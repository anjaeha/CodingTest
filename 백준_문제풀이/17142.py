from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 바이러스의 위치를 넣어줌
candi_virus = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            candi_virus.append((i, j))
        

# 바이러스 확산
def spread(arr):
    distance = [[-1] * n for _ in range(n)]
    visit = [[False] * n for _ in range(n)]
    q = deque()
    for i in range(len(arr)):
        visit[arr[i][0]][arr[i][1]] = True
        distance[arr[i][0]][arr[i][1]] = 0
        q.append(arr[i])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if visit[nx][ny] == False and graph[nx][ny] != 1:
                    distance[nx][ny] = distance[x][y] + 1
                    visit[nx][ny] = True
                    q.append((nx, ny))


    return distance

# 바이러스가 안퍼지는 경우가 있는지 확인 (벽이거나 바이러스면 안퍼짐)
def check(arr):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == -1:
                if graph[i][j] == 1 or graph[i][j] == 2:
                    continue
                else:
                    return False
    return True




# 백트래킹으로 바이러스를 선택할 수 있는 경우의수 탐색
result = 10000
use = [False] * len(candi_virus)
virus = []
def dfs(depth):
    global result
    if depth == m:
        # 바이러스 후보중 m개가 선택되어있는 상황임.
        temp = 0
        vir = spread(virus)
        if check(vir):
            for i in range(n):
                for j in range(n):
                    if temp < vir[i][j] and graph[i][j] != 2:
                        temp = vir[i][j]
            if result > temp:
                result = temp
        return


    
    for i in range(len(candi_virus)):
        if use[i]:
            continue

        use[i] = True
        virus.append((candi_virus[i]))
        dfs(depth + 1)
        
        virus.pop()
        for j in range(i + 1, len(candi_virus)):
            use[j] = False

dfs(0)

print(result if result != 10000 else -1)


"""
# 바이러스는 상하좌우로 동시에 복제
# M개를 활성화
# 모든 칸에 바이러스 퍼뜨리는데 걸리는 최소 시간 구하기
from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


virus = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            virus.append((i, j))
            graph[i][j] = '#'



def make_candi(depth): # M개의 바이러스를 선택하는 경우의 수
    global temp
    if depth == m:
        virus_pos.append(list(temp))
        return
    
    for i in range(len(virus)):
        if visit[i]:
            continue
        visit[i] = True
        temp.append(i)
        make_candi(depth + 1)
        temp.pop()
        for j in range(i + 1, len(virus)):
            visit[j] = False
virus_pos = []
temp = []
visit = [False] * len(virus)
make_candi(0)


def check(s):
    for i in range(n):
        for j in range(n):
            if s[i][j] == 0:
                if (i, j) in  virus:
                    continue
                else:
                    return False
    return True

def make_virus(arr):
    q = deque()
    s = [item[:] for item in graph]
    visit = [[False] * n for _ in range(n)]
    for i in range(len(arr)):
        q.append(virus[arr[i]])
        s[virus[arr[i]][0]][virus[arr[i]][1]] = 0
        visit[virus[arr[i]][0]][virus[arr[i]][1]] = True
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if (s[nx][ny] == 0 or s[nx][ny] == '#') and visit[nx][ny] == False:
                    s[nx][ny] = s[x][y] + 1
                    visit[nx][ny] = True
                    q.append((nx, ny))
    
    sec = 0
    flag = check(s)
    if flag:
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 0:
                    if s[i][j] > sec:
                        sec = s[i][j]
        return sec
    return -2

MIN = 1000000
for case in range(len(virus_pos)):
    arr = virus_pos[case]
    result = make_virus(arr)
    if result >= 0:
        MIN = min(MIN, result)

print(MIN if MIN != 1000000 else -1)
"""