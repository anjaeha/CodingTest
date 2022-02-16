from collections import deque

n = int(input())
target_x, target_y = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(x):
    visit = [False] * (n + 1)
    q = deque()
    q.append((x, 0))

    while q:
        x, idx = q.popleft()
        if x == target_y:
            return idx
        for i in graph[x]:
            if not visit[i]:
                q.append((i, idx + 1))
                visit[i] = True

answer = bfs(target_x)
print(answer if answer else -1)