# 교실의 크기는 N * N, 학생 수는 N ** 2
# 비어있는 칸 중, 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 이동
# 1이 여러개면, 인접한 칸 중에 비어있는 칸이 가장 많은 곳
# 2가 여러개면, 행이 작은순, 열이 작은 순

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
number = {}
for _ in range(n ** 2):
    temp = list(map(int, input().split()))
    number[temp[0]] = temp[1:]

graph = [[0] * n for _ in range(n)]

def condition(idx):
    s = [[0] * n for _ in range(n)]
    arr = number[idx]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]

                    if 0 <= nx < n and 0 <= ny < n:
                        if graph[nx][ny] in arr:
                            s[i][j] += 1
    MAX = -1
    for i in range(n):
        for j in range(n):
            MAX = max(MAX, s[i][j])

    pos = []
    for i in range(n):
        for j in range(n):
            if s[i][j] == MAX:
                pos.append((i, j))

    if len(pos) == 1:
        graph[pos[0][0]][pos[0][1]] = idx
        return

    empty = []
    for x, y in pos:
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 0:
                    cnt += 1
        empty.append((cnt, x, y))

    empty.sort(key = lambda x : (-x[0], x[1], x[2]))

    for i in range(len(empty)):
        if graph[empty[i][1]][empty[i][2]] == 0:
            graph[empty[i][1]][empty[i][2]] = idx
            break
    return

for rc, val in number.items():
    condition(rc)

result = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for d in range(4):
            nx = i + dx[d]
            ny = j + dy[d]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] in number[graph[i][j]]:
                    cnt += 1
        if cnt == 1:
            result += 1
        elif cnt == 2:
            result += 10
        elif cnt == 3:
            result += 100
        elif cnt == 4:
            result += 1000

print(result)