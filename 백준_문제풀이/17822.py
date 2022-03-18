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
    flag = False
    visit = [[False] * m for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(m):
            if graph[i][j] == 0:
                continue
            if i == 1:
                if graph[i][j] in [graph[i + 1][j], graph[i][(j - 1) % m], graph[i][(j + 1) % m]]:
                    now = graph[i][j]
                    visit[i][j] = True
                    if graph[i + 1][j] == now:
                        visit[i + 1][j] = True
                    if graph[i][(j + 1) % m] == now:
                        visit[i][(j + 1) % m] = True
                    if graph[i][(j - 1) % m] == now:
                        visit[i][(j - 1) % m] = True
                    flag = True
            elif i == n:
                if graph[i][j] in [graph[i - 1][j], graph[i][(j - 1) % m], graph[i][(j + 1) % m]]:
                    now = graph[i][j]
                    visit[i][j] = True
                    if graph[i - 1][j] == now:
                        visit[i - 1][j] = True
                    if graph[i][(j + 1) % m] == now:
                        visit[i][(j + 1) % m] = True
                    if graph[i][(j - 1) % m] == now:
                        visit[i][(j - 1) % m] = True
                    flag = True
            else:
                if graph[i][j] in [graph[i + 1][j], graph[i - 1][j], graph[i][(j - 1) % m], graph[i][(j + 1) % m]]:
                    now = graph[i][j]
                    visit[i][j] = True
                    if graph[i + 1][j] == now:
                        visit[i + 1][j] = True
                    if graph[i - 1][j] == now:
                        visit[i - 1][j] = True
                    if graph[i][(j + 1) % m] == now:
                        visit[i][(j + 1) % m] = True
                    if graph[i][(j - 1) % m] == now:
                        visit[i][(j - 1) % m] = True
                    flag = True
    if flag:
        for i in range(1, n + 1):
            for j in range(m):
                if visit[i][j]:
                    graph[i][j] = 0
    else:
        not_zero = []
        for i in range(1, n + 1):
            for j in range(m):
                if graph[i][j] != 0:
                    not_zero.append(graph[i][j])
        if not_zero:
            avg = sum(not_zero) / len(not_zero)
        else: # 다 0인 상태
            return

        for i in range(1, n + 1):
            for j in range(m):
                if graph[i][j] != 0:
                    if graph[i][j] < avg:
                        graph[i][j] += 1
                    elif graph[i][j] > avg:
                        graph[i][j] -= 1

    return


n, m, t = map(int, input().split()) # 가로M, 세로N
graph = [[0 for _ in range(m)]] + [list(map(int, input().split())) for _ in range(n)]
for i in range(t):
    x, d, k = map(int, input().split()) # x의 배수를, 시계(0) 또는 반시계(1) 방향으로, k칸 돌려라
    rotate(x, d, k)
    remove_number()


result = 0
for i in range(1, n + 1):
    for j in range(m):
        result += graph[i][j]
print(result)