import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visit = set((x, y))
    time = 0
    shark = 2
    eat = 0
    flag = False
    answer = 0

    while q:
        size = len(q)
        q = deque(sorted(q))

        for _ in range(size):
            x, y = q.popleft()

            if s[x][y] != 0 and s[x][y] < shark:
                eat += 1
                s[x][y] = 0

                if eat == shark:
                    shark += 1
                    eat = 0

                q = deque()
                visit = set((x, y))
                flag = True

                answer = time

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visit:
                    if s[nx][ny] <= shark:
                        q.append((nx, ny))
                        visit.add((nx, ny))

            if flag:
                flag = False
                break

        time += 1
    return answer

for i in range(n):
    for j in range(n):
        if s[i][j] == 9:
            xfish, yfish = i, j
            s[i][j] = 0

answer = bfs(xfish, yfish)
print(answer)