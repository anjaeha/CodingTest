from collections import deque
def bfs(x):
    q = deque()
    q.append(x)

    while q:
        x = q.popleft()
        for i in graph[x]:
            if parent[i] == 0:
                q.append(i)
                parent[i] = x

n = int(input())

graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

parent = [0] * (n + 1)

bfs(1)
for i in range(2, n + 1):
    print(parent[i])