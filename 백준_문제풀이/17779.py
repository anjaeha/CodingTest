n = int(input())
graph = [[]]
for _ in range(n):
    temp = [0] + list(map(int, input().split()))
    graph.append(temp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 상, 하, 좌, 우

def div(x, y, d1, d2): # 5구역 구하기
    for _ in range(d1): # 남서방향 대각선
        x = x + dx[1]
        y = y + dy[2]
        if 0 <= x < n + 1 and 0 <= y < n + 1:
            visit[x][y] = True
        else:
            return False
    for _ in range(d2): # 남동방향 대각선
        x = x + dx[1]
        y = y + dy[3]
        if 0 <= x < n + 1 and 0 <= y < n + 1:
            visit[x][y] = True
        else:
            return False
    for _ in range(d1):
        x = x + dx[0]
        y = y + dy[3]
        if 0 <= x < n + 1 and 0 <= y < n + 1:
            visit[x][y] = True
        else:
            return False
    for _ in range(d2):
        x = x + dx[0]
        y = y + dy[2]
        if 0 <= x < n + 1 and 0 <= y < n + 1:
            visit[x][y] = True
        else:
            return False

    for i in range(x + 1, x + d1 + d2):
        flag = False
        for j in range(n):
            if visit[i][j]:
                flag = not flag
            if flag:
                visit[i][j] = True

    return visit

def count(x, y, d1, d2, visit): # 각 구역의 인구수 구하기
    city = [0, 0, 0, 0, 0]

    for r in range(1, n + 1):
        for c in range(1, n + 1):
            if visit[r][c]:
                city[4] += graph[r][c]
            else:
                if 1 <= r < x + d1 and 1 <= c <= y:
                    city[0] += graph[r][c]
                elif 1 <= r <= x + d2 and y < c <= n:
                    city[1] += graph[r][c]
                elif x + d1 <= r <= n and 1 <= c < y - d1 + d2:
                    city[2] += graph[r][c]
                elif x + d2 < r <= n and y - d1 + d2 <= c <= n:
                    city[3] += graph[r][c]

    return city

MIN = int(1e9)
for x in range(1, n + 1):
    for y in range(1, n + 1):
        for d1 in range(1, n + 1):
            for d2 in range(1, n + 1):
                if 1 <= x < x + d1 + d2 <= n and 1 <= y - d1 < y < y + d2 <= n:
                    visit = [[False] * (n + 1) for _ in range(n + 1)]
                    visit = div(x, y, d1, d2)
                    city = count(x, y, d1, d2, visit)
                    MIN = min(MIN, max(city) - min(city))
print(MIN)