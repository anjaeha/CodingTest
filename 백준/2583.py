M, N, K = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
cnt = []

graph = [[0] * N for _ in range(M)]

for case in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1


for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            graph[i][j] = 1
            count = 1
            queue = [[i, j]]

            while queue:
                x, y = queue[0][0], queue[0][1]
                del queue[0]
                
                for k in range(4):
                    x1 = x + dx[k]
                    y1 = y + dy[k]

                    if 0 <= x1 < M and 0 <= y1 < N and graph[x1][y1] == 0:
                        graph[x1][y1] = 1
                        queue.append([x1, y1])
                        count += 1
            cnt.append(count)

cnt.sort()
print(len(cnt))
print(*cnt)
