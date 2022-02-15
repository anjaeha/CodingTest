def dfs(x):
    visit[x] = True
    for i in graph[x]:
        if not visit[i]:
            dfs(i)

from collections import deque
def bfs(x):
    q = deque()
    q.append(x)

    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visit[i]:
                q.append(i)
                visit[i] = True

n, m = map(int, input().split()) # 정점의 개수 N, 간선의 개수 M
graph = [[] for _ in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


visit = [False] * (n + 1)
answer = 0
for i in range(1, n + 1):
    if visit[i]:
        continue
    for j in graph[i]:
        if not visit[j]:
            bfs(j)
    answer += 1

print(answer)