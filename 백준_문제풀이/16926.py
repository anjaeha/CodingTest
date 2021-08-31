n, m, r = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

for _ in range(r):
    for i in range(min(n, m) // 2):
        s_x, s_y = i, i
        s_value = graph[s_x][s_y]

        for j in range(i + 1, n - i):
            s_x = j
            temp = graph[s_x][s_y]
            graph[s_x][s_y] = s_value
            s_value = temp

        for j in range(i + 1, m - i):
            s_y = j
            temp = graph[s_x][s_y]
            graph[s_x][s_y] = s_value
            s_value = temp


        for j in range(n - i - 2, i - 1, -1):
            s_x = j
            temp = graph[s_x][s_y]
            graph[s_x][s_y] = s_value
            s_value = temp

        for j in range(m - i - 2, i - 1, -1):
            s_y = j
            temp = graph[s_x][s_y]
            graph[s_x][s_y] = s_value
            s_value = temp

for i in graph:
    print(*i)