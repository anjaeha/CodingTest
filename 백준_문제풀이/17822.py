n, m, t = map(int, input().split())
graph = [[]] + [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def rotate(x, d, k):
    global graph
    for idx in range(x, n + 1, x):
        temp = graph[idx]
        for j in range(k): # k칸 돌려라
            if d == 0:
                temp.insert(0, temp.pop())
            elif d == 1:
                temp.append(temp.pop(0))
        graph[idx] = temp
    return

def remove_number():
    global graph
    copy_graph = [i[:] for i in graph]
    for x in range(1, n + 1):
        for y in range(m):
            for d in range(4):
                if d == 0 and x == 1:
                    continue
                if d == 1 and x == n:
                    continue
                nx = x + dx[d]
                ny = (y + dy[d]) % m
                if 1 <= nx < n + 1 and 0 <= ny < m:
                    if graph[x][y] == graph[nx][ny]:
                        copy_graph[nx][ny] = 0
                        copy_graph[x][y] = 0

    if graph == copy_graph:
        SUM = 0
        cnt = 0
        for i in range(1, n + 1):
            for j in range(m):
                if graph[i][j] > 0:
                    SUM += graph[i][j]
                    cnt += 1

        for i in range(1, n + 1):
            for j in range(m):
                if graph[i][j] > 0:
                    if graph[i][j] > (SUM / cnt):
                        graph[i][j] -= 1
                    elif graph[i][j] < (SUM / cnt):
                        graph[i][j] += 1
    else:
        graph = copy_graph

for _ in range(t):
    x, d, k = map(int, input().split())
    rotate(x, d, k)
    remove_number()

result = 0
for i in range(1, n + 1):
    for j in range(m):
        result += graph[i][j]

print(result)