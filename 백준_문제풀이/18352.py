import sys
input = sys.stdin.readline
from collections import deque

n, m, k, x = map(int, input().split())
s = [[] for _ in range(n+1)]
visit = [-1] * (n+1)
visit[x] = 0

for _ in range(m):
    a, b = map(int, input().split())
    s[a].append(b)

q = deque([x])

while q:
    now = q.popleft()

    for next in s[now]:
        if visit[next] == -1:
            visit[next] = visit[now] + 1
            q.append(next)

flag = False
for i in range(1, n+1):
    if visit[i] == k:
        print(i)
        flag = True

if not flag:
    print(-1)