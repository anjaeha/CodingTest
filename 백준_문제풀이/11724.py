N, M = map(int, input().split())

s = [[0] * (N+1) for _ in range(N+1)]
visit = [0 for i in range(N+1)]
cnt = 0

def dfs(i):
    visit[i] = 1
    for k in range(1, N+1):
        if s[i][k] == 1 and visit[k] == 0:
            dfs(k)


for case in range(M):
    a1, a2 = map(int, input().split())
    s[a1][a2] = 1
    s[a2][a1] = 1


for i in range(1, N+1):
    if visit[i] == 0:
        dfs(i)
        cnt += 1
    
print(cnt)

"""
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[0] * (n+1) for _ in range(n+1)]
visit = [0] * (n+1)

for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

def bfs(v):
    q = deque()
    q.append(v)
    visit[v] = 1

    while q:
        x = q.popleft()

        for i in range(1, n+1):
            if visit[i] == 0 and graph[x][i] == 1:
                q.append(i)
                visit[i] = 1
cnt = 0
for i in range(1, n+1):
    if visit[i] == 0:
        bfs(i)
        cnt += 1

print(cnt)
"""