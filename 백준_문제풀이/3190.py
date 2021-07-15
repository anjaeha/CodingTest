import sys
input = sys.stdin.readline
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# 오른, 아래, 왼, 위

def move():
    time = 0
    snake = deque()
    snake.append((0, 0))
    dir = 0
    x, y = 0, 0
    while 1:
        time += 1
        x = x + dx[dir]
        y = y + dy[dir]

        if x < 0 or y < 0 or x >= n or y >= n:
            break

    # 빈공간 : 0, 사과 : 1, 뱀 : 2
        if s[x][y] == 0:
            s[x][y] = 2
            snake.append((x, y))
            del_x, del_y = snake.popleft()
            s[del_x][del_y] = 0
        elif s[x][y] == 1:
            s[x][y] = 2
            snake.append((x, y))
        elif s[x][y] == 2:
            break

        
        if len(snake_dir) != 0 and snake_dir[0][0] == time:
            move_time, move_dir = snake_dir.pop(0)
            if move_dir == 'L':
                dir = (dir - 1) % 4
            elif move_dir == 'D':
                dir = (dir + 1) % 4
            
    return time


n = int(input())
s = [[0] * n for _ in range(n)]
k = int(input())

for _ in range(k):
    x, y = map(int, input().split())
    s[x - 1][y - 1] = 1

l = int(input())
snake_dir = []
for _ in range(l):
    x, y = input().strip().split()
    snake_dir.append((int(x), y))

print(move())