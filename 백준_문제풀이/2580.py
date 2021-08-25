import sys
input = sys.stdin.readline

graph = [list(map(int, input().split())) for _ in range(9)]
zero = []
for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            zero.append((i, j))

def candidate(x, y):
    temp = [i for i in range(1, 10)]
    for i in range(9):
        if graph[x][i] in temp:
            temp.remove(graph[x][i])
        if graph[i][y] in temp:
            temp.remove(graph[i][y])
    
    x_3 = x // 3
    y_3 = y // 3

    for i in range(x_3 * 3, x_3 * 3+ 3):
        for j in range(y_3 * 3, y_3 *3 + 3):
            if graph[i][j] in temp:
                temp.remove(graph[i][j])
    return temp

def dfs(count):
    if count == len(zero):
        for row in graph:
            print(*row)
        exit()
    (x, y) = zero[count]
    candi = candidate(x, y)
    for num in candi:
        graph[x][y] = num
        dfs(count + 1)
        graph[x][y] = 0

dfs(0)