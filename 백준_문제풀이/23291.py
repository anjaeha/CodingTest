# 물고기가 가장 적은 모든 어항에 + 1
# 두개 이상 쌓인 모든 블록을 공중 부양해서 90회전
# 물고기 수 조절 => 물고기 수의 차이 // 5 만큼 이동
# N / 2의 왼쪽블록을 180도 회전(역순)하여 오른쪽 블록에 올리기 X 2번
# 가장 많이 들어있는 물고기 - 가장 적게 들어있는 물고기 <= K가 되기 위해 몇번을 하는지 구하기
from collections import deque
from copy import deepcopy
n, k = map(int, input().split())
graph = deque(deque() for _ in range(n))
graph[0].extend(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def add_fish():
    MIN = min(graph[0])
    for i in range(n):
        if graph[0][i] == MIN:
            graph[0][i] += 1

def replace_bowl():
    global graph
    graph[1].append(graph[0].popleft()) # 첫번째는 직접 올려줌

    while 1:
        cnt = 0
        for i in range(len(graph)):
            if graph[i]:
                cnt += 1
                now = len(graph[i])
            else:
                break
        if len(graph[0]) - now < cnt:
            break
        for i in range(len(graph[1]), 0, -1):
            arr = []
            for j in range(cnt):
                arr.append(graph[j].popleft())
            graph[i].extend(arr)

    new_graph = deepcopy(graph)
    for x in range(len(graph)):
        for y in range(len(graph[x])):
            if graph[x] and y <= len(graph[x]):

                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < len(graph) and 0 <= ny < len(graph[nx]):
                        if graph[x][y] > graph[nx][ny]:
                            new_graph[nx][ny] += (graph[x][y] - graph[nx][ny]) // 5
                            new_graph[x][y] -= (graph[x][y] - graph[nx][ny]) // 5
    graph = new_graph

    arr = []
    while graph[0]:
        for i in range(len(graph)):
            if graph[i]:
                arr.append(graph[i].popleft())
    graph[0].extend(arr)

    arr = []
    for i in range(n // 2):
        arr.append(graph[0].popleft())
    graph[1].extend(arr[::-1])


    arr =[[] for _ in range(2)]
    for i in range(2):
        for j in range(n // 4):
            arr[i].append(graph[i].popleft())

    new_arr = [i[:] for i in arr]
    for x in range(len(arr)):
        for y in range(len(arr[0])):
            new_arr[x][y] = arr[len(arr) - x - 1][len(arr[0]) - 1 - y]

    for i in range(len(new_arr)):
        graph[2 + i].extend(new_arr[i])

    new_graph = deepcopy(graph)
    for x in range(len(graph)):
        for y in range(len(graph[x])):
            if graph[x] and y <= len(graph[x]):

                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < len(graph) and 0 <= ny < len(graph[nx]):
                        if graph[x][y] > graph[nx][ny]:
                            new_graph[nx][ny] += (graph[x][y] - graph[nx][ny]) // 5
                            new_graph[x][y] -= (graph[x][y] - graph[nx][ny]) // 5
    graph = new_graph

    arr = []
    while graph[0]:
        for i in range(len(graph)):
            if graph[i]:
                arr.append(graph[i].popleft())
    graph[0].extend(arr)

def check():
    if max(graph[0]) - min(graph[0]) <= k:
        return True
    return False

result = 0
while 1:
    if check():
        break
    add_fish()
    result += 1
    replace_bowl()

print(result)