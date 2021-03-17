N = int(input())
M = int(input())

graph = [[0] * (N+1) for _ in range(N+1)]

visit = [0 for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1


def dfs(k):
    visit[k] = 1
    for i in range(1, N+1):
        if graph[k][i] == 1 and visit[i] == 0:
            dfs(i)
            


dfs(1)
cnt = 0
for i in range(2, N+1):
    if visit[i] == 1:
        cnt += 1

print(cnt)

