
from copy import deepcopy
n, m, k = map(int, input().split())
n -= 1
m -= 1
graph = [list(map(int, input().split())) for _ in range(3)]

# R연산
def R_sort():
    # 숫자 세기
    length = len(graph[0])
    for i in range(len(graph)):
        temp = dict()
        for j in range(length):
            if graph[i][j] == 0:
                continue
            if graph[i][j] in temp:
                temp[graph[i][j]] += 1
            else:
                temp[graph[i][j]] = 1
        temp = sorted(temp.items(), key = lambda x : (x[1], x[0]))
        s = []
        for x, y in temp:
            s.append(x)
            s.append(y)
        graph[i] = deepcopy(s[:100])
    
    # 가장 긴 행 찾기
    MAX = -1
    for i in range(len(graph)):
        if len(graph[i]) > MAX:
            MAX = len(graph[i])
    # 0 추가해주기
    for i in range(len(graph)):
        while len(graph[i]) != MAX and len(graph[i]) <= 100:
            graph[i].append(0)

# C연산
def C_sort():
    global graph
    # 열을 행으로 바꿔서 진행
    copy_graph = []
    for i in range(len(graph[0])):
        temp = []
        for j in range(len(graph)):
            temp.append(graph[j][i])
        copy_graph.append(list(temp))

    # 숫자 세기
    length = len(copy_graph[0])
    for i in range(len(copy_graph)):
        temp = dict()
        for j in range(length):
            if copy_graph[i][j] == 0:
                continue
            if copy_graph[i][j] in temp:
                temp[copy_graph[i][j]] += 1
            else:
                temp[copy_graph[i][j]] = 1
        temp = sorted(temp.items(), key = lambda x : (x[1], x[0]))
        s = []
        for x, y in temp:
            s.append(x)
            s.append(y)
        copy_graph[i] = deepcopy(s[:100])
    
    # 가장 긴 행 찾기
    MAX = -1
    for i in range(len(copy_graph)):
        if len(copy_graph[i]) > MAX:
            MAX = len(copy_graph[i])
    # 0 추가해주기
    for i in range(len(copy_graph)):
        while len(copy_graph[i]) != MAX and len(copy_graph[i]) <= 100:
            copy_graph[i].append(0)
    temp_graph = []
    for i in range(len(copy_graph[0])):
        tmp = []
        for j in range(len(copy_graph)):
            tmp.append(copy_graph[j][i])
        temp_graph.append(list(tmp))
    graph = deepcopy(temp_graph)    

# 걸린 시간
result = 0
while 1:
    # R연산과 C연산을 반복하다보면 행의 수와 열의 수가 n, m보다 작아질 수 있음.
    if len(graph) >= (n + 1) and len(graph[0]) >= (m + 1):
        if graph[n][m] == k:
            break
    # 100초가 넘어가면 -1 출력
    if result > 100:
        result = -1
        break
    result += 1
    # 열의 개수와 행의 개수 비교
    if len(graph) >= len(graph[0]):
        R_sort()
    else:
        C_sort()
print(result)
