import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
a, b = map(int, input().split())
t = int(input())
graph = [[] for _ in range(n+1)]
visit = [0] * (n+1)

for i in range(t):
    p, c = map(int, input().split())
    graph[p].append(c)
    graph[c].append(p)


def bfs(start, end):
    q = deque()
    q.append(start)
    visited = []

    while q:
        x = q.popleft()
        visited.append(x)

        if x == end:
            break

        for c in graph[x]:
            if c not in visited:
                visit[c] = visit[x] + 1
                q.append(c)

    if visit[end] == 0:
        print(-1)
    else:
        print(visit[end])

bfs(a, b)
