import sys

r, c = map(int, input().split())
arr = [list(map(lambda x: ord(x) - 65, input())) for _ in range(r)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

check = [0] * 26
check[arr[0][0]] = 1

ans = 1

def dfs(x, y, cnt):
    global ans

    ans = max(ans, cnt)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c and check[arr[nx][ny]] == 0:
            check[arr[nx][ny]] = 1
            dfs(nx, ny, cnt+1)
            check[arr[nx][ny]] = 0

dfs(0, 0, ans)
print(ans)