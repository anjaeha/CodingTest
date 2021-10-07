
n = int(input())
graph = [[0] * (n + 1)]
for i in range(n):
    temp = [0]
    temp += list(map(int, input().split()))
    graph.append(temp)


def d(x, y, d1, d2):
    temp = [[0] * (n + 1) for _ in range(n + 1)]
    # 각 구역에 인원 파악하기 위한 변수
    p = [0] * 6 
    # 5번 구역 선긋기 왼쪽 대각선 두개
    for i in range(d1 + 1):
        temp[x + i][y - i] = 5
        temp[x + d2 + i][y + d2 - i] = 5
    # 오른쪽 대각선 두개
    for i in range(d2 + 1):
        temp[x + d1 + i][y - d1 + i] = 5
        temp[x + i][y + i] = 5
    # 경계선안에 포함되는 구역 x + 1부터 5를 만나면 안에 칠하고 다시 만나면 안칠하고..
    for i in range(x + 1, x + d1 + d2):
        flag = False
        for j in range(1, n + 1):
            if temp[i][j] == 5:
                flag = not flag
            if flag:
                temp[i][j] = 5

    # 모든 구역 돌아다니며 기준에 따라 p에 더해줌
    for r in range(1, n + 1):
        for c in range(1, n + 1):
            if temp[r][c] == 5:
                p[5] += graph[r][c]
            elif temp[r][c] == 0:
                if 1 <= r < x + d1 and 1 <= c <= y:
                    p[1] += graph[r][c]
                elif 1 <= r <= x + d2 and y < c <= n:
                    p[2] += graph[r][c]
                elif x + d1 <= r <= n and 1 <= c < y - d1 + d2:
                    p[3] += graph[r][c]
                elif x + d2 < r <= n and y - d1 + d2 <= c <= n:
                    p[4] += graph[r][c]
    return max(p[1:]) - min(p[1:])


result = 10000000000
for x in range(1, n + 1):
    for y in range(1, n + 1):
        for d1 in range(1, n + 1):
            for d2 in range(1, n + 1):
                if 1 <= x < x + d1 + d2 <= n and 1 <= y - d1 < y < y + d2 <= n:
                    temp = d(x, y, d1, d2)
                    if result > temp:
                        result = temp
print(result)


""" 경계선을 긋는 또 다른 방법 / 왼쪽, 오른쪽, 오른쪽, 왼쪽 방향으로 x, y값을 +- 1하며 돌려줌.
visit = [[False] * (n + 1) for _ in range(n + 1)]
    visit[x][y] = True
    nx, ny = x, y
    for i in range(d1):
        nx, ny = nx + 1, ny - 1
        visit[nx][ny] = True
    for i in range(d2):
        nx, ny = nx + 1, ny + 1
        visit[nx][ny] = True
    for i in range(d1):
        nx, ny = nx - 1, ny + 1
        visit[nx][ny] = True
    for i in range(d2):
        nx, ny = nx - 1, ny - 1
        visit[nx][ny] = True
    
    for i in range(x + 1, x + d1 + d2):
        flag = False
        for j in range(1, n + 1):
            if visit[i][j]:
                flag = not flag
            if flag:
                visit[i][j] = True
"""