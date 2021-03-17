from collections import deque

m, n = map(int, input().split())

t = []
queue = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    t.append(list((map(int, input().split()))))


def bfs():
    while queue:
        a, b = queue.popleft()

        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]

            if 0 <= x < n and 0 <= y < m and t[x][y] == 0:
                t[x][y] = t[a][b] + 1
                queue.append([x,y])

for i in range(n):
    for j in range(m):
        if t[i][j] == 1:
            queue.append([i, j])

bfs() # 여기까지 토마토 익히기.

isTrue = False
result = -2

for i in t:
    for j in i:
        if j == 0:
            isTrue = True
        result = max(result, j)

if isTrue == True:
    print(-1)
    #익지 못하는 상황
elif result == -1:
    print(0)
    # 이미 다 익어있음.
else:
    print(result - 1)