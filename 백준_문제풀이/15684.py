n, m, h = map(int, input().split()) # 세로선의 개수 N, 선의 개수 M, 가로선을 놓을 수 있는 위치 h
graph = [[False] * n for _ in range(h)] # 세로의 길이H, 가로의 길이N

for i in range(m):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = True

def check():
    for i in range(n):
        pos = i
        for j in range(h):
            if graph[j][pos]:
                pos += 1
            elif pos > 0 and graph[j][pos - 1]:
                pos -= 1
        if pos != i:
            return False
    return True

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
                graph[i][j] = True
                dfs(depth + 1, i, j)
                graph[i][j] = False
        y = 0

result = 4
dfs(0, 0, 0)
print(result if result < 4 else -1)