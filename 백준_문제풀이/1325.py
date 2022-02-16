from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[y].append(x)


def bfs(x):
    visit = [False] * (n + 1)
    visit[x] = True
    cnt = 1
    q = deque()
    q.append(x)
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visit[i]:
                visit[i] = True
                q.append(i)
                cnt += 1
    return cnt

answer = []
for i in range(1, n + 1):
    cnt = bfs(i)
    answer.append(cnt)

MAX = max(answer)
result = []
for i in range(len(answer)):
    if answer[i] == MAX:
        result.append(i + 1)
print(*result)