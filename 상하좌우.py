n = int(input())
walk = list(input().split())
x, y = 1, 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = ['L', 'R', 'U', 'D']

for i in walk:
    for j in range(4):
        if i == move[j]:
            nx = dx[j] + x
            ny = dy[j] + y

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x, y)
