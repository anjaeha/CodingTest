from collections import deque

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

sdx = [0, 1, 0, -1] # 상어 움직이는 방향
sdy = [-1, 0, 1, 0]

def crush(d, s): #
    for i in range(1, s + 1):
        nx = sx + dx[d] * i
        ny = sy + dy[d] * i
        graph[nx][ny] = 0

def ball_boom():
    global graph
    x, y, sd = sx, sy, 0
    q = deque()
    for idx in range(2 * n - 1):
        if idx == 2 * (n - 1):
            count = idx // 2
        else:
            count = idx // 2 + 1

        for i in range(count):
            x = x + sdx[sd]
            y = y + sdy[sd]
            if graph[x][y] != 0:
                q.append(graph[x][y])
        sd = (sd + 1) % 4

    while 1:
        nq = deque()
        stack = []
        for i in range(len(q)):
            if stack:
                if q[i] == stack[-1]:
                    stack.append(q[i])
                else:
                    if len(stack) >= 4:
                        marble[stack[-1]] += len(stack)
                        stack = [q[i]]
                    else:
                        nq.extend(stack)
                        stack = [q[i]]
            else:
                stack.append(q[i])
        if len(stack) >= 4:
            marble[stack[-1]] += len(stack)
        else:
            nq.extend(stack)
        if nq == q:
            break
        else:
            q = nq

    stack = []
    nq = deque()
    while q:
        x = q.popleft()
        if stack:
            if stack[-1] == x:
                stack.append(x)
            else:
                nq.extend((len(stack), stack[-1]))
                stack = [x]
        else:
            stack.append(x)
    if stack:
        nq.extend((len(stack), stack[-1]))

    board = [[0] * n for _ in range(n)]
    x, y, sd = sx, sy, 0
    for idx in range(2 * n - 1):
        if idx == 2 * (n - 1):
            count = idx // 2
        else:
            count = idx // 2 + 1

        for i in range(count):
            x = x + sdx[sd]
            y = y + sdy[sd]
            if nq:
                board[x][y] = nq.popleft()
            else:
                board[x][y] = 0
        sd = (sd + 1) % 4

    graph = board

# 폭발하는 구슬은 4개 이상 연속할때
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
sx, sy = n // 2, n // 2 # 상어의 위치
marble = [0] * 4
for _ in range(m):
    d, s = map(int, input().split())
    crush(d, s)
    ball_boom()


result = 0
for i in range(4):
    result += marble[i] * i
print(result)