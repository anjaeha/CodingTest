INF = int(1e9)


def solution(n, s, a, b, fares):
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                graph[i][j] = 0

    for i in fares:
        x, y, z = i
        graph[x][y] = z
        graph[y][x] = z

    for k in range(1, n + 1):
        for x in range(1, n + 1):
            for y in range(1, n + 1):
                graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])

    answer = INF
    for i in range(1, n + 1):
        result = graph[s][i] + graph[i][a] + graph[i][b]
        answer = min(answer, result)

    return answer