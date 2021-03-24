n = int(input())
g = []
for i in range(n):
    g.append(list(map(int, input().split())))

ans = 10000
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

def ck(list):
    cnt = 0
    flow = []

    for flower in list:
        x = flower // n
        y = flower % n

        if x == 0 or x == n - 1 or y == 0 or y == n - 1:
            return 10000
        for i in range(5):
            flow.append((x+dx[i], y+dy[i]))
            cnt += g[x+dx[i]][y+dy[i]]

    if len(set(flow)) != 15:
        return 10000
    return cnt
        



for i in range(n*n):
    for j in range(i+1, n*n):
        for k in range(j+1, n*n):
            ans = min(ans, ck([i,j,k]))

print(ans)