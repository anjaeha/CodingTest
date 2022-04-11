n = int(input())
graph = [[]] + [[0] + list(map(int, input().split())) for _ in range(n)]

def vote(x, y, d1, d2):
    global result
    section = [[]] + [[0] * (n + 1) for _ in range(n)]
    for i in range(d1):
        x += 1
        y -= 1
        section[x][y] = 5
    for i in range(d2):
        x += 1
        y += 1
        section[x][y] = 5
    for i in range(d1):
        x -= 1
        y += 1
        section[x][y] = 5
    for i in range(d2):
        x -= 1
        y -= 1
        section[x][y] = 5
    for i in range(x + 1, x + d1 + d2):
        flag = False
        for j in range(1, n + 1):
            if section[i][j] == 5:
                flag = not flag
            if flag:
                section[i][j] = 5

    count = [0] * 5
    for r in range(1, n + 1):
        for c in range(1, n + 1):
            if section[r][c] == 5:
                count[4] += graph[r][c]
            elif 1 <= r < x + d1 and 1 <= c <= y:
                count[0] += graph[r][c]
            elif 1 <= r <= x + d2 and y < c <= n:
                count[1] += graph[r][c]
            elif x + d1 <= r <= n and 1 <= c < y - d1 + d2:
                count[2] += graph[r][c]
            elif x + d2 < r <= n and y - d1 + d2 <= c <= n:
                count[3] += graph[r][c]
    result = min(result, max(count) - min(count))

result = int(1e9)
for x in range(1, n):
    for y in range(1, n):
        for d1 in range(1, n):
            for d2 in range(1, n):
                if d1 >= 1 and d2 >= 1 and 1 <= x < x + d1 + d2 <= n and 1 <= y - d1 < y < y + d2 <= n:
                    vote(x, y, d1, d2)
print(result)