N, M, v = map(int, input().split())

t = [[0] * (N+1) for _ in range(N+1)]
visit = [0 for _ in range(N+1)]

for case in range(M):
    a, b = map(int, input().split())
    t[a][b] = 1
    t[b][a] = 1


def dfs(v):
    print(v, end = ' ')
    visit[v] = 1
    for i in range(1, N+1):
        if visit[i] == 0 and t[v][i] == 1:
            dfs(i)


def bfs(v):
    queue = [v]
    visit[v] = 1

    while queue:
        v = queue[0]
        print(v, end = ' ')
        del queue[0]
        for i in range(1, N+1):
            if visit[i] == 0 and t[v][i] == 1:
                queue.append(i)
                visit[i] = 1



dfs(v)
visit = [0 for _ in range(N+1)]
print()
bfs(v)