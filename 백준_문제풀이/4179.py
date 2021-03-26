from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    global q, f
    while q:
        temp = deque()
        while q:
            x, y = q.popleft()
            if (x == r - 1 or y == c - 1 or x == 0 or y == 0) and maze[x][y] != "F": return maze[x][y] + 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < r and 0 <= ny < c and maze[nx][ny] == '.' and maze[x][y] != "F":
                    temp.append([nx, ny])
                    maze[nx][ny] = maze[x][y] + 1

        q = temp
    
        temp = deque()
        while f:
            x, y = f.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < r and 0 <= ny < c and visit[nx][ny] == 0 and maze[nx][ny] != "#":
                    temp.append([nx, ny])
                    visit[nx][ny] = 1
                    maze[nx][ny] = "F"
        f = temp

r, c = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

maze = []

q = deque()
f = deque()
visit = [[0] * c for i in range(r)]

for i in range(r):
    a = list(input().strip())
    maze.append(a)
    for j in range(c):
        if a[j] == 'J':
            q.append([i, j])
            maze[i][j] = 0
        elif a[j] == 'F':
            f.append([i, j])
            visit[i][j] = 1

result = bfs()
print(result if result != None else "IMPOSSIBLE")