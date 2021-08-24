import sys
input = sys.stdin.readline

n, m, h = map(int, input().split())
line = [list(map(int, input().split())) for _ in range(m)]

dx = [0, 0]
dy = [-1, 1]
# 왼쪽, 오른쪽

result = 0

graph = [[0] * n for _ in range(h)]

for x, y in line:
    graph[x-1][y-1] = 1

# 사다리타고 내려오기
def move(number):
    x, y = 0, number
    while 1:
        if graph[x][y] == 1:
            for i in range(2):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] == 1:
                        x, y = nx + 1, ny
        else:
            x += 1

        if x >= h:
            break
    return y

def check():
    for start in range(n):
        k = start
        for i in range(h):
            if graph[i][k]:
                k += 1
            elif k > 0 and graph[i][k-1]:
                k -= 1
        if start != k:
            return False
    return True

result = 4

def dfs(cnt, x, y):
    global result
    if check():
        result = min(result, cnt)
        return
    elif cnt >= 3:
        return
    
    for i in range(x, h):
        if i == x:
            k = y
        else:
            k = 0
        for j in range(k, n - 1):
            if graph[i][j] == 0 and graph[i][j+1] == 0:
                graph[i][j] = 1
                dfs(cnt + 1, i, j + 2)
                graph[i][j] = 0
            


dfs(0, 0, 0)
print(result if result < 4 else - 1)