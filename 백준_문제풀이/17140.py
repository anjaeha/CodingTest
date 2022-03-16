# R 연산 - 행을 정렬, 행의 개수 >= 열의 개수인 경우에 적용
# C 연산 - 열을 정렬, 행의 개수 < 열의 개수인 경우에 적용
# 연산을 적용하고 가장 큰 배열의 길이에 맞춰 0으로 채움 (0은 정렬할때 무시)
# 크기가 100을 넘어가면 버리기

r, c, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(3)]
# graph[r][c] == k가 되는 최소 연산 시간 구하기 (100초 넘으면 - 1)

def row_sort():
    global graph
    for idx in range(len(graph)):
        count = {}
        arr = graph[idx]
        for j in arr:
            if j == 0:
                continue
            if j in count:
                count[j] += 1
            else:
                count[j] = 1

        sort_arr = sorted(count.items(), key = lambda x : (x[1], x[0]))
        arr = []
        for rc, val in sort_arr:
            arr.extend((rc, val))

        graph[idx] = arr
    long = -1
    for idx in range(len(graph)):
        long = max(long, len(graph[idx]))

    for i in range(len(graph)):
        for _ in range(long - len(graph[i])):
            graph[i].append(0)

def col_sort():
    global graph
    board = []
    for i in range(len(graph[0])):
        arr = []
        for j in range(len(graph)):
            arr.append(graph[j][i])
        board.append(arr)

    for idx in range(len(board)):
        count = {}
        arr = board[idx]
        for j in arr:
            if j == 0:
                continue
            if j in count:
                count[j] += 1
            else:
                count[j] = 1

        sort_arr = sorted(count.items(), key = lambda x : (x[1], x[0]))
        arr = []
        for rc, val in sort_arr:
            arr.extend((rc, val))

        board[idx] = arr
    long = -1
    for idx in range(len(board)):
        long = max(long, len(board[idx]))

    for i in range(len(board)):
        for _ in range(long - len(board[i])):
            board[i].append(0)

    new_graph = []
    for i in range(len(board[0])):
        arr = []
        for j in range(len(board)):
            arr.append(board[j][i])
        new_graph.append(arr)
    graph = new_graph


result = 0
while 1:
    if len(graph) > (r - 1) and len(graph[0]) > (c - 1):
        if graph[r - 1][c - 1] == k:
            break

    if result > 100:
        result = -1
        break
    if len(graph) >= len(graph[0]):
        row_sort()
    else:
        col_sort()

    result += 1

print(result)