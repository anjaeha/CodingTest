# 시계방향으로 90도
# 얼음3개 이상과 인접해있지않은칸 - 1
# 남아있는 얼음합, 가장 큰 덩어리의 크기
from copy import deepcopy
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 주위에 얼음이 몇개있지 확인
def check_arouond(x, y):
    count = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 2 ** n and 0 <= ny < 2 ** n:
            if temp[nx][ny] > 0:
                count += 1
    if count >= 3:
        return True
    else:
        return False

# 가장 큰 사이즈 구하기
def find_size(x, y):
    tmp = 1
    q = deque()
    q.append((x, y))
    visit[x][y] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 2 ** n and 0 <= ny < 2 ** n:
                if graph[nx][ny] > 0 and visit[nx][ny] == False:
                    q.append((nx, ny))
                    visit[nx][ny] = True
                    tmp += 1
    return tmp



# n의 크기에 따라 그래프 돌리기
def turn_graph(l):
    if l == 0:
        return graph
    else:
        s = [[0] * (2 ** n) for _ in range(2 ** n)]
        for i in range (0, 2 ** n, 2 ** l):
            for j in range(0, 2 ** n, 2 ** l):
                for i2 in range(2 ** l):
                    for j2 in range(2 ** l):
                        s[i + i2][j + j2] = graph[i + 2 ** l - j2 - 1][j + i2]
        return s
        

       
n, q = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(2 ** n)]
l_num = list(map(int, input().split()))

for case in range(q):
    temp = turn_graph(l_num[case])
    graph = deepcopy(temp)
    for i in range(2 ** n):
        for j in range(2 ** n):
            if check_arouond(i, j):
                continue
            else:
                graph[i][j] -= 1


visit = [[False] * (2 ** n) for _ in range(2 ** n)]
result = 0
siz = 0
for i in range(2 ** n):
    for j in range(2 ** n):
        if graph[i][j] > 0:
            result += graph[i][j]
            if visit[i][j] == False:
                kk = find_size(i, j)
            if kk > siz:
                siz = kk

print(result)
print(siz)