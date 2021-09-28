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

graph = [list(map(int, input().split())) for _ in range(n)]
visit = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, depth):
    global MAX, temp, max_val
    if depth == 4:
        if MAX < temp:
            MAX = temp
        return

    if temp + max_val * (4 - depth) < MAX: # 현재 temp에 주어진 종이 위에 있는 최대값을 다 더해도 MAX보다 작다면 중간에 종료한다.
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if not visit[nx][ny]:
                if depth == 2:
                    visit[nx][ny] = True
                    temp += graph[nx][ny]
                    dfs(x, y, depth + 1)
                    temp -= graph[nx][ny]
                    visit[nx][ny] = False
                    
                temp += graph[nx][ny]
                visit[nx][ny] = True
                dfs(nx, ny, depth + 1)
                temp -= graph[nx][ny]
                visit[nx][ny] = False

max_val = -1
for i in range(n):
    for j in range(m):
        if max_val < graph[i][j]:
            max_val = graph[i][j]

MAX = -1
for i in range(n):
    for j in range(m):
        visit[i][j] = True
        temp = graph[i][j]
        dfs(i, j, 1)
        visit[i][j] = False


print(MAX)
"""