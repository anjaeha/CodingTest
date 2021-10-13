# 1 ~ 5 블록, 6 ~ 10 웜홀, -1 블랙홀
# 출발위치와 방향 선택하여 최대값 구하기
# 빈 공간에서 시작해야함.

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 상, 하, 좌, 우
def move(sx, sy, d):
    x, y = sx, sy
    answer = 0

    while 1:
        nx = x + dx[d]
        ny = y + dy[d]

        if nx == -1 or ny == -1 or nx == n or ny == n:
            return (answer * 2 + 1)

        if nx == sx and ny == sy:
            return answer
        
        if graph[nx][ny] == 0:
            x, y = nx, ny
            continue
        elif graph[nx][ny] == 1:
            answer += 1
            if d == 0:
                d ^= 1
            elif d == 1:
                d = 3
            elif d == 2:
                d = 0
            elif d == 3:
                d ^= 1
        elif graph[nx][ny] == 2:
            answer += 1
            if d == 0:
                d = 3
            elif d == 1:
                d ^= 1
            elif d == 2:
                d = 1
            elif d == 3:
                d ^= 1
        elif graph[nx][ny] == 3:
            answer += 1
            if d == 0:
                d = 2
            elif d == 1:
                d ^= 1
            elif d == 2:
                d ^= 1
            elif d == 3:
                d = 1
        elif graph[nx][ny] == 4:
            answer += 1
            if d == 0:
                d ^= 1
            elif d == 1:
                d = 2
            elif d == 2:
                d ^= 1
            elif d == 3:
                d = 0
        elif graph[nx][ny] == 5:
            answer += 1
            d ^= 1
        elif 6 <= graph[nx][ny] <= 10:
            for p in portal[graph[nx][ny]]:
                if p != [nx, ny]:
                    nx, ny = p[0], p[1]
                    break
        elif graph[nx][ny] == -1:
            return answer

        x, y = nx, ny

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]

    result = -1
    zeros = []
    portal = {}
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                zeros.append((i, j))
            elif 6 <= graph[i][j] <= 10:
                if portal.get(graph[i][j]) is None:
                    portal[graph[i][j]] = [[i, j]]
                else:
                    portal[graph[i][j]].append([i, j])


    for x, y in zeros:
        for d in range(4):
            temp = move(x, y, d)
            result = max(result, temp)
    print("#%d %d" %(tc, result))