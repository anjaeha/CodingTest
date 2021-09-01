from copy import deepcopy

def archer(cnt): # 궁수 배치 경우의 수
    global idx
    if cnt == 3:
        idx.append(list(temp))
        return
    
    for i in range(m):
        if visit[i]:
            continue
        
        visit[i] = True
        temp.append(number[i])
        archer(cnt + 1)
        temp.pop()

        for j in range(i + 1, m):
            visit[j] = False



n, m, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
graph += [[0] * m]
graph_copy = deepcopy(graph)
number = [i for i in range(m)]
visit = [False] * m
idx = []
temp = []
archer(0)


MAX = -1
for case in range(len(idx)):
    graph = deepcopy(graph_copy)
    result = 0
    a1, a2, a3 = idx[case]
    graph[n][a1] = 3
    graph[n][a2] = 3
    graph[n][a3] = 3
    k = 0

    while 1:
        flag = 0
        for i in range(n - k):
            flag += sum(graph[i])
        if flag == 0:
            break
        remove1 = []
        remove2 = []
        remove3 = []

        
        for i in range(n - 1 - k, n -k - d - 1, -1):
            for j in range(m):
                if i >= 0 and j >= 0 and graph[i][j] == 1:
                    if abs(n - i - k) + abs(a1 - j) <= d:
                        remove1.append((i, j, abs(n - i - k) + abs(a1 - j)))
                    if abs(n - i - k) + abs(a2 - j) <= d:
                        remove2.append((i, j, abs(n - i - k) + abs(a2 - j)))
                    if abs(n - i - k) + abs(a3 - j) <= d:
                        remove3.append((i, j, abs(n - i - k) + abs(a3 - j)))
        remove1.sort(key = lambda x : (x[2], x[1]))
        remove2.sort(key = lambda x : (x[2], x[1]))
        remove3.sort(key = lambda x : (x[2], x[1]))

        if remove1:
            del1 = remove1.pop(0)
            x, y, c = del1
            if graph[x][y] == 1:
                graph[x][y] = 0
                result += 1
        if remove2:
            del2 = remove2.pop(0)
            x, y, c = del2
            if graph[x][y] == 1:
                graph[x][y] = 0
                result += 1
        if remove3:
            del3 = remove3.pop(0)
            x, y, c = del3
            if graph[x][y] == 1:
                graph[x][y] = 0
                result += 1
        k += 1
    MAX = max(MAX, result)
        
print(MAX)
