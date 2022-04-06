n, m, h = map(int, input().split())
graph = [[0] * n for _ in range(h)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = 1

def check():
    for idx in range(n):
        pos = idx
        for i in range(h):
            if graph[i][pos]:
                pos += 1
            elif pos > 0 and graph[i][pos - 1]:
                pos -= 1
        if pos != idx:
            return False
    return True

result = 4
def dfs(depth, x, y):
    global result
    if result <= depth:
        return

    if check():
        result = depth
        return

    if depth == 3:
        return

    for i in range(x, h):
        for j in range(y, n - 1):
            if not graph[i][j] and not graph[i][j + 1]:
                graph[i][j] = 1
                dfs(depth + 1, i, j)
                graph[i][j] = 0
        y = 0

dfs(0, 0, 0)
print(result if result < 4 else -1)