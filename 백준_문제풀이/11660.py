n, m = map(int, input().split())
graph = [[0] * (n + 1)]
for _ in range(n):
    temp = [0]
    temp += list(map(int, input().split()))
    graph.append(temp)
point = [list(map(int, input().split())) for _ in range(m)]


board = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        board[i][j] = board[i - 1][j] + board[i][j - 1] - board[i - 1][j - 1] + graph[i][j]

for i in range(m):
    x1, y1, x2, y2 = point[i]
    result = board[x2][y2] - (board[x2][y1 - 1] + board[x1 - 1][y2] - board[x1 - 1][y1 - 1])
    print(result)