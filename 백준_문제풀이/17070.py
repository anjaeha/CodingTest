n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)] # 0 - 빈칸, 1 - 벽

def dfs(x, y, d):
    global answer
    if x == n - 1 and y == n - 1:
        answer += 1
        return

    if d == 0 or d == 2: # 가로 방향이거나 대각선 방향일 때
        if y + 1 < n:
            if graph[x][y + 1] == 0:
                dfs(x, y + 1, 0) # 가로 방향으로 밀기

    if d == 1 or d == 2: # 세로 방향이거나 대각선 방향일 때
        if x + 1 < n:
            if graph[x + 1][y] == 0:
                dfs(x + 1, y, 1) # 세로 방향으로 밀기

    if d == 0 or d == 1 or d == 2: # 가로, 세로, 대각선 방향일 때
        if x + 1 < n and y + 1 < n:
            if graph[x + 1][y + 1] == 0 and graph[x][y + 1] == 0 and graph[x + 1][y] == 0: # 주변에 벽이 없어야함
                dfs(x + 1, y + 1, 2) # 대각선으로 밀기


answer = 0
dfs(0, 1, 0)
print(answer)