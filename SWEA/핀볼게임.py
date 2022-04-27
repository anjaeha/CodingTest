from collections import deque

T = int(input())

dx = [-1, 1, 0, 0] # 상 하 좌 우
dy = [0, 0, -1, 1]

def move(sx, sy, d):
    q = deque()
    q.append((sx, sy, d))
    cnt = 0

    while q:
        x, y, d = q.popleft()
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == -1 or (nx, ny) == (sx, sy):
                return cnt

            if graph[nx][ny] == 0:
                q.append((nx, ny, d))
            elif graph[nx][ny] == 1:
                if d == 0 or d == 3:
                    return cnt * 2 + 1
                elif d == 1:
                    q.append((nx, ny, 3))
                elif d == 2:
                    q.append((nx, ny, 0))
                cnt += 1

            elif graph[nx][ny] == 2:
                if d == 1 or d == 3:
                    return cnt * 2 + 1
                elif d == 0:
                    q.append((nx, ny, 3))
                elif d == 2:
                    q.append((nx, ny, 1))
                cnt += 1

            elif graph[nx][ny] == 3:
                if d == 1 or d == 2:
                    return cnt * 2 + 1
                elif d == 0:
                    q.append((nx, ny, 2))
                elif d == 3:
                    q.append((nx, ny, 1))
                cnt += 1

            elif graph[nx][ny] == 4:
                if d == 0 or d == 2:
                    return cnt * 2 + 1
                elif d == 1:
                    q.append((nx, ny, 2))
                elif d == 3:
                    q.append((nx, ny, 0))
                cnt += 1

            elif graph[nx][ny] == 5:
                return cnt * 2 + 1

            else:
                for rr, cc in holl[graph[nx][ny]]:
                    if (nx, ny) != (rr, cc):
                        q.append((rr, cc, d))
        else:
            return cnt * 2 + 1

for tc in range(T):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]

    holl = {}
    for x in range(n):
        for y in range(n):
            if 6 <= graph[x][y] <= 10:
                if graph[x][y] in holl:
                    holl[graph[x][y]].append((x, y))
                else:
                    holl[graph[x][y]] = [(x, y)]

    result = -1
    for r in range(n):
        for c in range(n):
            if graph[r][c] == 0:
                for d in range(4):
                    result = max(result, move(r, c, d))

    print("#%d %d" %(tc + 1, result))