from collections import deque

n, m, v = map(int, input().split())
visit = [0 for _ in range(n+1)]
s = [[0] * (n+1) for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    s[x][y] = 1
    s[y][x] = 1

def dfs(v):
    print(v, end = ' ')
    visit[v] = 1

    for i in range(1, n+1):
        if visit[i] == 0 and s[v][i] == 1:
            dfs(i)


def bfs(v):
    q = deque()
    q.append(v)
    visit[v] = 0

    while q:
        a = q.popleft()
        print(a, end = ' ')

        for i in range(1, n+1):
            if visit[i] == 1 and s[a][i] == 1:
                q.append(i)
                visit[i] = 0

dfs(v)
print()
bfs(v)