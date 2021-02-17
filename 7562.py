from collections import deque

dx = [2, 2, -2, -2, -1, -1, 1, 1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]



T = int(input())

def bfs(sx, sy, ax, ay):
    queue = deque()
    queue.append([sx, sy])
    s[sx][sy] = 1

    while queue:
        a, b = queue.popleft()

        if a == ax and b == ay:
            print(s[ax][ay] - 1)
            return
        

        for i in range(8):
            x = a + dx[i]
            y = b + dy[i]

            if 0 <= x < l and 0 <= y < l and s[x][y] == 0:
                queue.append([x, y])
                s[x][y] = s[a][b] + 1

for case in range(T):
    l = int(input())
    sx, sy = map(int, input().split())
    ax, ay = map(int, input().split())
    s = [[0] * l for _ in range(l)]
    bfs(sx, sy, ax, ay)
