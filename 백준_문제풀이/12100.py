from collections import deque

def move(dir):
    if dir == 0: # 위로 움직이기
        for y in range(n):
            arr = deque()
            for x in range(n):
                if graph[x][y]:
                    arr.append(graph[x][y])
                    graph[x][y] = 0
            for x in range(n):
                if arr:
                    graph[x][y] = arr.popleft()
                    if arr:
                        if arr[0] == graph[x][y]:
                            graph[x][y] *= 2
                            arr.popleft()
    elif dir == 1: # 아래로 움직이기
        for y in range(n):
            arr = deque()
            for x in range(n - 1, -1, -1):
                if graph[x][y]:
                    arr.append(graph[x][y])
                    graph[x][y] = 0
            for x in range(n - 1, -1, -1):
                if arr:
                    graph[x][y] = arr.popleft()
                    if arr:
                        if arr[0] == graph[x][y]:
                            graph[x][y] *= 2
                            arr.popleft()

    elif dir == 2: # 왼쪽으로 움직이기
        for x in range(n):
            arr = deque()
            for y in range(n):
                if graph[x][y]:
                    arr.append(graph[x][y])
                    graph[x][y] = 0
            for y in range(n):
                if arr:
                    graph[x][y] = arr.popleft()
                    if arr:
                        if arr[0] == graph[x][y]:
                            graph[x][y] *= 2
                            arr.popleft()
    elif dir == 3: # 오른쪽로 움직이기
        for x in range(n):
            arr = deque()
            for y in range(n - 1, -1, -1):
                if graph[x][y]:
                    arr.append(graph[x][y])
                    graph[x][y] = 0
            for y in range(n - 1, -1, -1):
                if arr:
                    graph[x][y] = arr.popleft()
                    if arr:
                        if arr[0] == graph[x][y]:
                            graph[x][y] *= 2
                            arr.popleft()

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

result = 0

def dfs(depth):
    global result, graph
    if depth == 5:
        for i in range(n):
            result = max(result, max(graph[i]))
        return

    temp_graph = [i[:] for i in graph]
    for d in range(4):
        move(d)
        dfs(depth + 1)
        graph = [i[:] for i in temp_graph]

dfs(0)
print(result)