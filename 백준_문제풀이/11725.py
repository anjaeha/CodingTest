from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

p = [0] * (n + 1)

q = deque([1])
while q:
    x = q.popleft()

    for i in range(len(graph[x])):
        if p[graph[x][i]] == 0:
            p[graph[x][i]] = x
            q.append(graph[x][i])


for i in range(2, n + 1):
    print(p[i])