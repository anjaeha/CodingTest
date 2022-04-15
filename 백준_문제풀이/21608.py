n = int(input())
number = {}
for i in range(n ** 2):
    temp = list(map(int, input().split()))
    number[temp[0]] = temp[1:]

# 좋아하는 학생이 가장 많이 인접한 칸 -> 공백이 많은 칸 -> 가장 작은 행, 열
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
graph = [[0] * n for _ in range(n)]

def check(idx, x, y):
    c = 0
    z = 0
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] in number[idx]:
                c += 1
            elif graph[nx][ny] == 0:
                z += 1
    return c, z

for idx, val in number.items():
    candi = [] # 몇명이 인접했는지, 공백이 몇개인지, 행과 열 저장
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                c, z = check(idx, i, j)
                candi.append((c, z, i, j))
    candi.sort(key = lambda x : (-x[0], -x[1], x[2], x[3]))
    graph[candi[0][2]][candi[0][3]] = idx

result = 0
for i in range(n):
    for j in range(n):
        idx = graph[i][j]
        c, z = check(idx, i, j)
        result += int(10 ** (c - 1))

print(result)