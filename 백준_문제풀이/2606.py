n = int(input())

s = [[0] * (n+1) for _ in range(n+1)]
visit = [0 for _ in range(n+1)]

for _ in range(int(input())):
    x, y = map(int, input().split())
    s[x][y] = 1
    s[y][x] = 1

cnt = -1

def dfs(v):
    global cnt
    cnt += 1
    visit[v] = 1

    for i in range(1, n+1):
        if s[v][i] == 1 and visit[i] == 0:
            dfs(i)


dfs(1)
print(cnt)