r, c, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(3)]

def cal_r():
    global graph
    MAX = 0
    for idx in range(len(graph)):
        arr = graph[idx]
        new_arr = {}
        for i in arr:
            if i == 0:
                continue
            if i in new_arr:
                new_arr[i] += 1
            else:
                new_arr[i] = 1
        new_arr = sorted(new_arr.items(), key=lambda x : (x[1], x[0]))
        temp = []
        for x, y in new_arr:
            temp.extend((x, y))
        graph[idx] = temp
        MAX = max(MAX, len(temp))

    for idx in range(len(graph)):
        for i in range(MAX - len(graph[idx])):
            graph[idx].append(0)

def cal_c():
    global graph
    new_graph = [[] for _ in range(len(graph[0]))]
    MAX = 0
    for idx in range(len(graph[0])):
        arr = []
        for i in range(len(graph)):
            arr.append(graph[i][idx])

        new_arr = {}
        for i in arr:
            if i == 0:
                continue
            if i in new_arr:
                new_arr[i] += 1
            else:
                new_arr[i] = 1
        new_arr = sorted(new_arr.items(), key=lambda x: (x[1], x[0]))
        temp = []
        for x, y in new_arr:
            temp.extend((x, y))
        new_graph[idx] = temp
        MAX = max(MAX, len(temp))

    for idx in range(len(new_graph)):
        for i in range(MAX - len(new_graph[idx])):
            new_graph[idx].append(0)

    graph = [[0] * len(new_graph) for _ in range(len(new_graph[0]))]
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            graph[i][j] = new_graph[j][i]

result = 0
while 1:
    if len(graph) > r - 1 and len(graph[0]) > c - 1:
        if graph[r - 1][c - 1] == k:
            break
    if result > 100:
        result = -1
        break

    if len(graph) >= len(graph[0]):
        cal_r()
    else:
        cal_c()
    result += 1

print(result)