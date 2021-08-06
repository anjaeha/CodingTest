import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = []

for i in range(n):
    for j in range(n):
        if s[i][j] == 9:
            heappush(q, (0, i, j))
            s[i][j] = 0
            break


def bfs():
    body, eat, answer = 2, 0, 0
    check = [[False] * n for _ in range(n)]

    while q:
        d, x, y = heappop(q)

        if 0 < s[x][y] < body:
            eat += 1
            s[x][y] = 0
            if eat == body:
                body += 1
                eat = 0
            answer += d
            d = 0

            while q:
                q.pop()
            check = [[False] * n for _ in range(n)]

        for i in range(4):
            nd = d + 1
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if check[nx][ny] or body < s[nx][ny]:
                continue

            heappush(q, (nd, nx, ny))
            check[nx][ny] = True

    print(answer)

bfs()