import sys
input = sys.stdin.readline
from collections import deque

a, b = map(int, input().split())
n, m = map(int, input().split())

dist = [-1] * (n+1)
s = [[] for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    s[x].append(y)
    s[y].append(x)


def bfs():
    q = deque()
    q.append(a)
    dist[a] = 0

    while q:
        x = q.popleft()

        if x == b:
            print(dist[b])
            return

        for i in s[x]:
            if dist[i] == -1:
                q.append(i)
                dist[i] = dist[x] + 1
    print(-1)

bfs()