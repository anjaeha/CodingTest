import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]
cheese = []

def find():
    q = deque()
    q.append((0, 0))
    visit = [[False] * m for _ in range(n)]
    visit[0][0] = True
    cnt = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
                if s[nx][ny] == 1:
                    s[nx][ny] = 0
                    cnt += 1
                elif s[nx][ny] == 0:
                    q.append((nx, ny))

                visit[nx][ny] = True
    
    cheese.append(cnt)
    return cnt

time = 0
while 1:
    time += 1
    cnt = find()
    if cnt == 0:
        break

print(time - 1)
print(cheese[-2])