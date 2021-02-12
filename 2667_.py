N = int(input())

apt = []
city = []
cnt = 0

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]



for i in range(N):
    city.append(list(map(int,input())))


def dfs(i, j):
    global cnt
    city[i][j] = 0
    cnt += 1

    for k in range(4):
        a = i + dx[k]
        b = j + dy[k]

        if a < 0 or a >= N or b < 0 or b >= N:
            continue

        if city[a][b] == 1:
            dfs(a, b)


for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            cnt = 0
            dfs(i, j)
            apt.append(cnt)


print(len(apt))
apt.sort()
for i in range(len(apt)):
    print(apt[i])