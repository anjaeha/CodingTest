import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

apt = []
city = []
cnt = 0

n = int(input())

for i in range(n):
    city.append(list(map(int, input().strip())))

def dfs(x ,y):
    global cnt
    cnt += 1
    city[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and city[nx][ny] == 1:
            dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            cnt = 0
            dfs(i, j)
            apt.append(cnt)


apt.sort()
print(len(apt))
for i in apt:
    print(i)