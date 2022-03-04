from collections import deque
def move(d):
    if d == 0: # 위로 올렸을때
        q = deque()
        for i in range(n):
            for j in range(n):
                if graph[j][i]:
                    q.append(graph[j][i])
                    graph[j][i] = 0
            answer = deque()
            while q:
                temp = q.popleft()
                if q:
                    if temp == q[0]:
                        answer.append(temp * 2)
                        q.popleft()
                    else:
                        answer.append(temp)
                else:
                    answer.append(temp)
            for j in range(n):
                if answer:
                    graph[j][i] = answer.popleft()
                else:
                    graph[j][i] = 0
    elif d == 1: # 아래로 내렸을 때
        q = deque()
        for i in range(n):
            for j in range(n - 1, -1, -1):
                if graph[j][i]:
                    q.append(graph[j][i])
                    graph[j][i] = 0
            answer = deque()
            while q:
                temp = q.popleft()
                if q:
                    if temp == q[0]:
                        answer.append(temp * 2)
                        q.popleft()
                    else:
                        answer.append(temp)
                else:
                    answer.append(temp)
            for j in range(n - 1, -1, -1):
                if answer:
                    graph[j][i] = answer.popleft()
                else:
                    graph[j][i] = 0
    elif d == 2: # 왼쪽으로 밀었을때
        q = deque()
        for i in range(n):
            for j in range(n):
                if graph[i][j]:
                    q.append(graph[i][j])
                    graph[i][j] = 0
            answer = deque()
            while q:
                temp = q.popleft()
                if q:
                    if temp == q[0]:
                        answer.append(temp * 2)
                        q.popleft()
                    else:
                        answer.append(temp)
                else:
                    answer.append(temp)
            for j in range(n):
                if answer:
                    graph[i][j] = answer.popleft()
                else:
                    graph[i][j] = 0
    elif d == 3: # 왼쪽으로 밀었을때
        q = deque()
        for i in range(n):
            for j in range(n - 1, -1, -1):
                if graph[i][j]:
                    q.append(graph[i][j])
                    graph[i][j] = 0
            answer = deque()
            while q:
                temp = q.popleft()
                if q:
                    if temp == q[0]:
                        answer.append(temp * 2)
                        q.popleft()
                    else:
                        answer.append(temp)
                else:
                    answer.append(temp)
            for j in range(n - 1, -1, -1):
                if answer:
                    graph[i][j] = answer.popleft()
                else:
                    graph[i][j] = 0

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

MAX = -1
def dfs(depth):
    global MAX, graph
    if depth == 5:
        for i in range(n):
            MAX = max(MAX, max(graph[i]))
        return

    board = [item[:] for item in graph]
    for d in range(4):
        move(d)
        dfs(depth + 1)
        graph = [item[:] for item in board]

dfs(0)
print(MAX)