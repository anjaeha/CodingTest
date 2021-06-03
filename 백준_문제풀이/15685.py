import sys
input = sys.stdin.readline

n = int(input())
s = [[0] * 101 for _ in range(101)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


for _ in range(n):
    x, y, d, g = map(int, input().split())
    s[x][y] = 1
    move = [d]

    for _ in range(g):
        q = []
        for i in range(len(move)):
            q.append((move[-1-i] + 1) % 4)
        move.extend(q)

    for i in move:
        nx = x + dx[i]
        ny = y + dy[i]
        s[nx][ny] = 1
        x, y = nx, ny

result = 0
for i in range(100):
    for j in range(100):
        if s[i][j] == 1:
            if s[i+1][j] == 1 and s[i+1][j+1] == 1 and s[i][j+1] == 1:
                result += 1

print(result)