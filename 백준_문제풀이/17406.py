from copy import deepcopy

def rotate(x, y, r):
    for i in range(r):
        min_x = x - r + i
        max_x = x + r - i
        min_y = y - r + i
        max_y = y + r - i
        
        s_x, s_y = x - r + i, y - r + i

        val = graph[min_x][min_y]

        for ny in range(min_y + 1, max_y + 1):
            temp = graph[s_x][ny]
            graph[s_x][ny] = val
            val = temp
            s_y = ny
        
        for nx in range(min_x + 1, max_x + 1):
            temp = graph[nx][s_y]
            graph[nx][s_y] = val
            val = temp
            s_x = nx

        for ny in range(max_y - 1, min_y - 1, -1):
            temp = graph[s_x][ny]
            graph[s_x][ny] = val
            val = temp
            s_y = ny

        for nx in range(max_x - 1, min_x - 1, -1):
            temp = graph[nx][s_y]
            graph[nx][s_y] = val
            val = temp
            s_x = nx

def find_min(min_val):
    for i in range(n):
        temp = sum(graph[i])
        min_val = min(temp, min_val)
    return min_val
            
n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cal = []
for i in range(k):
    a, b, c = map(int, input().split())
    cal.append([a - 1, b - 1, c])
answer = 50000

number = [i for i in range(k)]
array = []
visit = [False] * k
temp = []

def dfs(cnt):
    global array
    if cnt == k:
        array.append(list(temp))
        return

    for i in range(k):
        if visit[i]:
            continue
        
        visit[i] = True
        temp.append(number[i])
        dfs(cnt + 1)
        temp.pop()

        visit[i] = False

dfs(0)
min_val = 50000
for i in range(len(array)):
    graph_temp = deepcopy(graph)
    for j in range(k):
        tmp = cal[array[i][j]]
        a, b, c = tmp
        rotate(a, b, c)
    min_val = find_min(min_val)
    graph = graph_temp

print(min_val)