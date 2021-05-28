import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    q = deque()
    q.append(v)
    visit[v] = 1

    while q:
        x = q.popleft()

        for i in range(1, n+1):
            if visit[i] == 0 and f[x][i] == 1:
                q.append(i)
                visit[i] = visit[x] + 1
                
n = int(input())
m = int(input())

f = [[0] * (n+1) for _ in range(n+1)]
visit = [0] * (n+1)

for i in range(m):
    x, y = map(int, input().split())
    f[x][y] = 1
    f[y][x] = 1

bfs(1)

cnt = 0

for i in visit:
    if 1 < i <= 3:
        cnt += 1

print(cnt)