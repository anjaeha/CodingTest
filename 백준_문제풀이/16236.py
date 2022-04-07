from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            graph[i][j] = 0
            sx, sy = i, j
            break
size = 2
def find_food():
    dist = [[-1] * n for _ in range(n)]
    dist[sx][sy] = 0
    q = deque()
    q.append((sx, sy))
    food = []

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] <= size and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
                    if 0 < graph[nx][ny] < size:
                        food.append((dist[nx][ny], nx, ny))

    food.sort(key = lambda x : (x[0], x[1], x[2]))
    if food:
        return food[0]
    else:
        return False

result = 0
eat = 0
while 1:
    temp = find_food()
    if not temp:
        break
    result += temp[0]
    sx, sy = temp[1], temp[2]
    graph[sx][sy] = 0
    eat += 1
    if eat == size:
        size += 1
        eat = 0

print(result)