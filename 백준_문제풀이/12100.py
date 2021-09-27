from collections import deque
from copy import deepcopy

def move(dir):
    # 위로
    if dir == 0:
        q = deque()
        for i in range(n):
            for j in range(n):
                if graph[j][i]:
                    q.append(graph[j][i])
                    graph[j][i] = 0
            answer = []
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
                    graph[j][i] = answer.pop(0)
                else:
                    graph[j][i] = 0

    # 아래로             
    elif dir == 1:
        q = deque()
        for i in range(n):
            for j in range(n - 1, -1, -1):
                if graph[j][i]:
                    q.append(graph[j][i])
                    graph[j][i] = 0
            answer = []
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
                    graph[j][i] = answer.pop(0)
                else:
                    graph[j][i] = 0
    # 왼쪽으로
    elif dir == 2:
        q = deque()
        for i in range(n):
            for j in range(n):
                if graph[i][j]:
                    q.append(graph[i][j])
                    graph[i][j] = 0
            answer = []
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
                    graph[i][j] = answer.pop(0)
                else:
                    graph[i][j] = 0

    # 오른쪽으로
    elif dir == 3:
        q = deque()
        for i in range(n):
            for j in range(n - 1, -1, -1):
                if graph[i][j]:
                    q.append(graph[i][j])
                    graph[i][j] = 0
            answer = []
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
                    graph[i][j] = answer.pop(0)
                else:
                    graph[i][j] = 0


# 최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]


result = -1
def dfs(depth):
    global result, graph
    if depth == 5:
        for i in range(n):
            for j in range(n):
                if graph[i][j] > result:
                    result = graph[i][j]
        return

    temp = deepcopy(graph)
    for i in range(4):
        move(i)
        dfs(depth + 1)
        graph = deepcopy(temp)

dfs(0)
print(result)