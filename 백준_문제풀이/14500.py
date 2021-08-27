import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]

t = [
    [(0,0), (0,1), (1,0), (1,1)], # ㅁ
    [(0,0), (0,1), (0,2), (0,3)], # ㅡ
    [(0,0), (1,0), (2,0), (3,0)], # ㅣ
    [(0,0), (0,1), (0,2), (1,0)], 
    [(1,0), (1,1), (1,2), (0,2)],
    [(0,0), (1,0), (1,1), (1,2)], # ㄴ
    [(0,0), (0,1), (0,2), (1,2)], # ㄱ
    [(0,0), (1,0), (2,0), (2,1)],
    [(2,0), (2,1), (1,1), (0,1)],
    [(0,0), (0,1), (1,0), (2,0)], 
    [(0,0), (0,1), (1,1), (2,1)],
    [(0,0), (0,1), (0,2), (1,1)], # ㅜ
    [(1,0), (1,1), (1,2), (0,1)], # ㅗ
    [(0,0), (1,0), (2,0), (1,1)], # ㅏ
    [(1,0), (0,1), (1,1), (2,1)], # ㅓ
    [(1,0), (2,0), (0,1), (1,1)],
    [(0,0), (1,0), (1,1), (2,1)],
    [(1,0), (0,1), (1,1), (0,2)],
    [(0,0), (0,1), (1,1), (1,2)]
]

result = 0
for i in range(n):
    for j in range(m):
        for k in t:
            try:
                n = s[i + k[0][0]][j + k[0][1]] + s[i + k[1][0]][j + k[1][1]] + s[i + k[2][0]][j + k[2][1]] + s[i + k[3][0]][j + k[3][1]]
            except:
                n = 0
            result = max(n, result)

print(result)


"""
n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
visit = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(k, temp, x, y):
    global result

    if k == 4:
        result = max(result, temp)
        return

    if (4 - k) * max_val + temp < result:
        return


    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if not visit[nx][ny]:
                visit[nx][ny] = True
                if k == 2:
                    dfs(k + 1, temp + array[nx][ny], x, y)
                dfs(k + 1, temp + array[nx][ny], nx, ny)
                visit[nx][ny] = False
    return

max_val = -1
for i in range(n):
    for j in range(m):
        max_val = max(max_val, array[i][j])

result = 0
for i in range(n):
    for j in range(m):
        visit[i][j] = True
        dfs(1, array[i][j], i, j)
        visit[i][j] = False

print(result)
"""