N = int(input())

graph = [list(map(int, input())) for _ in range(N)]

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

cnt = 0
apt = []

def dfs(i, j):
    global cnt
    graph[i][j] = "0"
    cnt += 1

    for way in range(4):
        ii = i + dx[way] 
        jj = j + dy[way]
        if ii < 0 or ii >= N or jj < 0 or jj >= N:
            continue

        if graph[ii][jj] == 1:
            dfs(ii, jj)


for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            cnt = 0
            dfs(i, j)
            apt.append(cnt)

print(len(apt))
print('\n'.join(list(map(str, sorted(apt)))))