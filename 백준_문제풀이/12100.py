from collections import deque
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def slide(dir):
    q = deque()
    if dir == 0: # 위로
        for y in range(n):
            for x in range(n):
                if graph[x][y]:
                    q.append(graph[x][y])
            for x in range(n):
                if q:
                    graph[x][y] = q.popleft()
                    if q and q[0] == graph[x][y]:
                        graph[x][y] *= 2
                        q.popleft()
                else:
                    graph[x][y] = 0

    elif dir == 1: # 아래로
        for y in range(n):
            for x in range(n - 1, -1, -1):
                if graph[x][y]:
                    q.append(graph[x][y])
            for x in range(n - 1, -1, -1):
                if q:
                    graph[x][y] = q.popleft()
                    if q and q[0] == graph[x][y]:
                        graph[x][y] *= 2
                        q.popleft()
                else:
                    graph[x][y] = 0
    elif dir == 2: # 왼쪽으로
        for x in range(n):
            for y in range(n):
                if graph[x][y]:
                    q.append(graph[x][y])
            for y in range(n):
                if q:
                    graph[x][y] = q.popleft()
                    if q and q[0] == graph[x][y]:
                        graph[x][y] *= 2
                        q.popleft()
                else:
                    graph[x][y] = 0

    elif dir == 3: # 오른쪽으로
        for x in range(n):
            for y in range(n - 1, -1, -1):
                if graph[x][y]:
                    q.append(graph[x][y])
            for y in range(n - 1, -1, -1):
                if q:
                    graph[x][y] = q.popleft()
                    if q and q[0] == graph[x][y]:
                        graph[x][y] *= 2
                        q.popleft()
                else:
                    graph[x][y] = 0

def move(depth):
    global graph, result
    if depth == 5:
        for x in range(n):
            for y in range(n):
                if graph[x][y]:
                    result = max(result, graph[x][y])
        return
    board = [i[:] for i in graph]
    for i in range(4):
        slide(i)
        move(depth + 1)
        graph = [i[:] for i in board]

result = -1
move(0)
print(result)