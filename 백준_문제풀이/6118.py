import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
s = [[] for _ in range(n+1)]
visit = [0] * (n+1)

for i in range(m):
    x, y = map(int, input().split())
    s[x].append(y)
    s[y].append(x)

def bfs(v):
    q = deque()
    q.append(v)
    visit[v] = 1

    while q:
        x = q.popleft()

        for i in s[x]:
            if visit[i] == 0:
                q.append(i)
                visit[i] = visit[x] + 1

bfs(1)
k = max(visit)
print(visit.index(k), k - 1, visit.count(k))

