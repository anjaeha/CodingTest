from collections import deque

def blizard(d, s):
    x, y = n // 2, n // 2
    for i in range(s):
        nx = x + dx[d]
        ny = y + dy[d]
        graph[nx][ny] = 0
        x, y = nx, ny


def ball_exp():
    global sd, sx, sy, graph, ball
    q = deque()
    x, y = sx, sy
    sd = 0
    for case in range(2 * n - 1):
        if case == 2 * n - 2:
            time = case // 2
        else:
            time = case // 2 + 1

        for i in range(time):
            x = x + qdx[sd]
            y = y + qdy[sd]

            if graph[x][y] != 0:
                q.append(graph[x][y])
        sd = (sd + 1) % 4
    if not q:
        return

    while 1:
        flag = False
        que = deque()
        temp = []
        for i in range(len(q)):
            if temp == []:
                temp.append(q[i])
            else:
                if temp[0] == q[i]:
                    temp.append(q[i])
                else:
                    if len(temp) >= 4:
                        ball[temp[0]] += len(temp)
                        temp = [q[i]]
                        flag = True
                    else:
                        que.extend(temp)
                        temp = [q[i]]
        if len(temp) < 4:
            que.extend(temp)
        else:
            ball[temp[0]] += len(temp)

        if not flag:
            break
        q = que

    temp = []
    que = deque()
    for i in range(len(q)):
        if temp == []:
            temp.append(q[i])
        else:
            if temp[-1] == q[i]:
                temp.append(q[i])
            else:
                que.append(len(temp))
                que.append(temp[0])
                temp = [q[i]]
    que.append(len(temp))
    que.append(temp[0])

    board = [[0] * n for _ in range(n)]
    x, y = sx, sy
    sd = 0
    for case in range(2 * n - 1):
        if not que:
            continue
        if case == 2 * n - 2:
            time = case // 2
        else:
            time = case // 2 + 1

        for i in range(time):
            x = x + qdx[sd]
            y = y + qdy[sd]

            if que:
                board[x][y] = que.popleft()
            else:
                break
        sd = (sd + 1) % 4
    graph = board

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
exp = []
for _ in range(m):
    d, s = map(int, input().split())
    exp.append((d - 1, s))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

qdx = [0, 1, 0, -1]
qdy = [-1, 0, 1, 0]

sx, sy = n // 2, n // 2 # 상어의 위치
ball = [0, 0, 0, 0]

for t in range(m):
    dir, dis = exp[t]
    blizard(dir, dis)
    ball_exp()

result = 0
for i in range(1, 4):
    result += ball[i] * i

print(result)